import redis
import time
from isserviceup.config import config


def update_status():
    rclient = redis.from_url(config.REDIS_URL)
    services = config.SERVICES
    for service in services:
        status = service.get_status().name
        key = 'service:{}'.format(service.name)
        pipe = rclient.pipeline()
        pipe.hset(key, 'status', status)
        pipe.hset(key, 'last_update', time.time())
        pipe.execute()
    rclient.set('services:last_update', time.time())


if __name__ == '__main__':
    update_status()