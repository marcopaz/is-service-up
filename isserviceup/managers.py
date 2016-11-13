import redis
from mongoengine import connect

from isserviceup.config import config

rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)

connect(config.MONGO_URL.split('/')[-1], host=config.MONGO_URL)
