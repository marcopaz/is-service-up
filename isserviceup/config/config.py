from decouple import config
from isserviceup.services.aws import AWS
from isserviceup.services.compose import Compose
from isserviceup.services.gcloud import GCloud
from isserviceup.services.heroku import Heroku
from isserviceup.services.pingdom import Pingdom
from isserviceup.services.redislabs import RedisLabs
from isserviceup.services.sentry import Sentry

DEBUG = config('DEBUG', cast=bool, default=False)
REDIS_URL = config('REDIS_URL', default='redis://localhost')


SERVICES = [
    AWS(),
    GCloud(),
    Heroku(),
    RedisLabs(),
    Compose(),
    Sentry(),
    Pingdom(),
]
