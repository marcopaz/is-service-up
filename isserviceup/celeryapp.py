import logging
import time

import raven
import redis
from celery import Celery
from celery.utils.log import get_task_logger
from raven.conf import setup_logging
from raven.contrib.celery import register_signal, register_logger_signal
from raven.handlers.logging import SentryHandler

from isserviceup.config import celery as celeryconfig
from isserviceup.config import config
from isserviceup.storage.services import set_service_status, set_last_update
from isserviceup.services.models.service import Status

MAX_RETRIES = 3
DELAY_RETRY = 2

app = Celery('app')
app.config_from_object(celeryconfig)

logger = get_task_logger(__name__)
rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)

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


def set_service_status(service, status):
    key = 'service:{}'.format(service.name)
    pipe = rclient.pipeline()
    pipe.hget(key, 'status')
    pipe.hmset(key, {'status': status.name, 'last_update': time.time()})
    old_status = pipe.execute()[0]
    if old_status != status.name:
        broadcast_status_change.delay(service.name, old_status, status.name)


@app.task(name='update-services-status')
def update_services_status():
    set_last_update(rclient, time.time())
    for i in range(len(config.SERVICES)):
        update_service_status.delay(i)


@app.task(name='update-service-status', bind=True, max_retries=MAX_RETRIES)
def update_service_status(self, idx):
    service = config.SERVICES[idx]
    logger.info('Updating status for service {}'.format(service.name))
    try:
        status = service.get_status()
    except Exception as exc:
        if self.request.retries == MAX_RETRIES-1:  # last retry
            set_service_status(rclient, service, Status.unavailable)
            raise
        else:
            return self.retry(exc=exc, countdown=DELAY_RETRY)

    set_service_status(rclient, service, status)


@app.task(name='broadcast-status-change')
def broadcast_status_change(service, old_status, new_status):
    for i in range(len(config.NOTIFIERS)):
        notify_status_change.delay(i, service, old_status, new_status)


@app.task(name='notify-status-change')
def notify_status_change(idx, service, old_status, new_status):
    notifier = config.NOTIFIERS[idx]
    notifier.notify(service, old_status, new_status)


if __name__ == '__main__':
    app.start()
