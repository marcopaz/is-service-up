import redis
from isserviceup.config import config

rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)
