import requests
from decouple import config
from isserviceup.services.models.service import Service, Status


class WeblatePlugin(Service):

    icon_url = '/images/icons/weblate.png'

    def __init__(self):
        # Will check if the Weblate website is OK.
        self.check_http = config('WEBLATE_CHECK_HTTP', default=True, cast=bool)
        # Will check if the Weblate JSON API is OK.
        self.check_json = config('WEBLATE_CHECK_JSON', default=True, cast=bool)
        # If you need to monitor multiple Weblate instances and need each one
        # to have a different behaviour: extend this class, override the
        # __init__ function, call super, and then override these properties.

    def _check_http(self):
        request = requests.get(self.status_url)
        return request.ok

    def _check_json(self):
        request = requests.get('{base}/api/projects'.format(
            base=self.status_url.strip('/')
        ))
        try:
            if request.json():
                return True
        except ValueError as error:
            print('Value error: {msg}'.format(msg=error.message))
        return False

    def get_status(self):
        status = [
            not self.check_http or self._check_http(),
            not self.check_json or self._check_json(),
        ]
        if all(status):
            return Status.ok
        elif any(status):
            return Status.major
        return Status.critical
