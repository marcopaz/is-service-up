import time
from typing import List
import datetime
import redis

from isserviceup.services.models.service import Service, Status


_status_key = lambda service: 'service:{}'.format(service.name)
_last_update_key = 'services:last_update'


def set_last_update(client: redis.Redis, t: float):
    client.set(_last_update_key, t)


def set_service_status(client: redis.Redis, service: Service, status: Status):
    client.hmset(_status_key(service), {
        'status': status.name,
        'last_update': time.time(),
    })


def get_status(client: redis.Redis, services: List[Service]) -> (List[str], datetime.datetime):
    pipe = client.pipeline()
    for service in services:
        pipe.hget(_status_key(service), 'status')
    pipe.get(_last_update_key)
    values = pipe.execute()
    status = [Status[x] if x else None for x in values[:-1]]
    last_update = datetime.datetime.fromtimestamp(float(values[-1])) if values[-1] else None
    return status, last_update
