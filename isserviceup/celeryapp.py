import logging
import time

import raven
from celery import Celery
from celery.utils.log import get_task_logger
from raven.conf import setup_logging
from raven.contrib.celery import register_signal, register_logger_signal
from raven.handlers.logging import SentryHandler

from isserviceup import managers
from isserviceup.config import celery as celeryconfig
from isserviceup.config import config
from isserviceup.models.favorite import Favorite
from isserviceup.notifiers.slack import Slack
from isserviceup.services import SERVICES
from isserviceup.services.models.service import Status
from isserviceup.storage.services import set_service_status, set_last_update

MAX_RETRIES = 3
DELAY_RETRY = 2

app = Celery('app')
app.config_from_object(celeryconfig)

logger = get_task_logger(__name__)

if config.SENTRY_DSN:
    client = raven.Client(config.SENTRY_DSN)
    register_logger_signal(client, loglevel=logging.ERROR)
    register_signal(client)
    # report logging errors
    handler = SentryHandler(client)
    setup_logging(handler)
    # show sentry errors in the console
    logger = logging.getLogger('sentry.errors')
    logger.setLevel(logging.ERROR)
    logger.addHandler(logging.StreamHandler())


@app.task(name='update-services-status')
def update_services_status():
    set_last_update(managers.rclient, time.time())
    for service_id in SERVICES:
        update_service_status.delay(service_id)


@app.task(bind=True, max_retries=MAX_RETRIES)
def update_service_status(self, service_id):
    service = SERVICES[service_id]
    logger.info('Updating status for service {}'.format(service.name))
    try:
        status = service.get_status()
    except Exception as exc:
        if self.request.retries == MAX_RETRIES-1:  # last retry
            set_service_status(managers.rclient, service, Status.unavailable)
            raise
        else:
            return self.retry(exc=exc, countdown=DELAY_RETRY)

    logger.info('Service={} has status={}'.format(service.name, status.name))
    old_status = set_service_status(managers.rclient, service, status)
    if old_status is not None and old_status != status:
        broadcast_status_change.delay(service.id, old_status.name, status.name)


@app.task()
def broadcast_status_change(service_id, old_status, new_status):
    service = SERVICES[service_id]

    send_all_slack_notifications.delay(service_id, old_status, new_status)

    for i in range(len(config.NOTIFIERS)):
        notify_status_change.delay(i, service.name, old_status, new_status)


@app.task()
def notify_status_change(idx, service, old_status, new_status):
    notifier = config.NOTIFIERS[idx]
    notifier.notify(service, old_status, new_status)


@app.task()
def send_all_slack_notifications(service_id, old_status, new_status):
    favs = Favorite.objects(service_id=service_id,
                            slack_webhook__ne=None,
                            monitored_status__in=[new_status])
    for fav in favs:
        send_slack_notification.delay(fav.webhook_url, service_id, old_status, new_status)


@app.task()
def send_slack_notification(webhook_url, service_id, old_status, new_status):
    service = SERVICES[service_id]
    s = Slack(webhook_url)
    s.notify(service.name, old_status, new_status)


if __name__ == '__main__':
    app.start()
