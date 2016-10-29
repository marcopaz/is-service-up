import redis
import time
from isserviceup.config import config
rclient = redis.from_url(config.REDIS_URL)

services = config.SERVICES
for service in services:
    status = service.get_status().name
    key = 'service:{}'.format(service.name)
    pipe = rclient.pipeline()
    pipe.hmset(key, {'status': status, 'last_update': time.time()})
    pipe.execute()

rclient.set('services:last_update', time.time())