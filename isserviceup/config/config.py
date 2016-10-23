from decouple import config
from isserviceup.services.aws import AWS
from isserviceup.services.compose import Compose
from isserviceup.services.gcloud import GCloud
from isserviceup.services.heroku import Heroku
from isserviceup.services.pingdom import Pingdom
from isserviceup.services.redislabs import RedisLabs
from isserviceup.services.sentry import Sentry
from isserviceup.services.github import GitHub

DEBUG = config('DEBUG', cast=bool, default=False)
REDIS_URL = config('REDIS_URL', default='redis://redis:devpassword@redis')
GA_CODE = config('GA_CODE', default='UA-86164785-1')


SERVICES = [
    AWS(),
    GCloud(),
    GitHub(),
    Heroku(),
    RedisLabs(),
    Compose(),
    Sentry(),
    Pingdom(),
]
