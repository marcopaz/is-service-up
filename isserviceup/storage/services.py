import time
from typing import List
import datetime
import redis

from isserviceup.services.models.service import Service, Status


_status_key = lambda service: 'service:{}'.format(service.name)
_last_update_key = 'services:last_update'


def set_last_update(client: redis.Redis, t: float):
    client.set(_last_update_key, t)


def set_service_status(client: redis.Redis, service: Service, status: Status) -> Status:
    key = _status_key(service)
    pipe = client.pipeline()
    pipe.hget(key, 'status')
    pipe.hmset(key, {
        'status': status.name,
        'last_update': time.time(),
    })
    prev_status = pipe.execute()[0]
    if prev_status is not None:
        prev_status = Status[prev_status]
    return prev_status


def get_status(client: redis.Redis, services: List[Service]) -> (List[str], datetime.datetime):
    pipe = client.pipeline()
    for service in services:
        pipe.hget(_status_key(service), 'status')
    pipe.get(_last_update_key)
    values = pipe.execute()
    status = [Status[x] if x else None for x in values[:-1]]
    last_update = datetime.datetime.fromtimestamp(float(values[-1])) if values[-1] else None
    return status, last_update
