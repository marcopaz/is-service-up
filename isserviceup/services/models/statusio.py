import requests

from isserviceup.services.models.service import Service, Status


class StatusIOPlugin(Service):

    status_url = 'https://api.status.io/'

    @property
    def statuspage_id(self):
        raise NotImplemented()

    def get_status(self):
        r = requests.get('{}/1.0/status/{}'.format(
            self.status_url.strip("/"), self.statuspage_id
        ))
        try:
            j = r.json()
        except ValueError:
            print(r.content)
            raise
        expected_status = {
            100: Status.ok,
            200: Status.minor,
            300: Status.major,
            400: Status.critical,
            500: Status.critical,
            600: Status.maintenance,
        }
        try:
            status_code = j['result']['status_overall']['status_code']
            if status_code in expected_status:
                return expected_status[status_code]
            raise Exception('unexpected status')
        except KeyError:
            print(j)
            raise
