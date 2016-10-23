from isserviceup.services.aws import AWS
from isserviceup.services.compose import Compose
from isserviceup.services.gcloud import GCloud
from isserviceup.services.heroku import Heroku
from isserviceup.services.pingdom import Pingdom
from isserviceup.services.redislabs import RedisLabs
from isserviceup.services.sentry import Sentry

services = [
    Heroku(),
    GCloud(),
    AWS(),
    RedisLabs(),
    Compose(),
    Pingdom(),
    Sentry(),
]

for service in services:
    print('{}: status={} icon_url={}'.format(service.name, service.get_status(), service.get_icon_url()))
