import redis
import time

from celery.utils.log import get_task_logger

from isserviceup.config import celery as celeryconfig
from isserviceup.config import config
from celery import Celery


app = Celery('app')
app.config_from_object(celeryconfig)

logger = get_task_logger(__name__)
rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)


@app.task(name='update-services-status')
def update_services_status():
    rclient.set('services:last_update', time.time())
    for i in range(len(config.SERVICES)):
        update_service_status.delay(i)


@app.task(name='update-service-status', bind=True)
def update_service_status(self, idx):
    service = config.SERVICES[idx]
    logger.info('Updating status for service {}'.format(service.name))
    status = service.get_status().name
    key = 'service:{}'.format(service.name)
    pipe = rclient.pipeline()
    pipe.hset(key, 'status', status)
    pipe.hset(key, 'last_update', time.time())
    pipe.execute()


if __name__ == '__main__':
    app.start()
