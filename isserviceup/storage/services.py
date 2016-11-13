import time

from isserviceup.services.models.service import Status


_status_key = lambda service: 'service:{}'.format(service.name)
_last_update_key = 'services:last_update'


def set_last_update(client, t):
    client.set(_last_update_key, t)


def set_service_status(client, service, status):
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


def get_status(client, services):
    pipe = client.pipeline()
    for service in services:
        pipe.hget(_status_key(service), 'status')
    values = pipe.execute()
    status = [Status[x] if x else None for x in values]
    return status
