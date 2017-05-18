from decouple import config
from isserviceup.services.models.weblate import WeblatePlugin


class Weblate(WeblatePlugin):

    name = config('WEBLATE_SERVICE_NAME', default='Weblate')
    status_url = config('WEBLATE_URL', default='https://demo.weblate.com/')
