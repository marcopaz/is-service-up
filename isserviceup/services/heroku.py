import requests

from isserviceup.services.models.service import Service, Status


class Heroku(Service):
    name = 'Heroku'
    status_url = 'https://status.heroku.com/'
    icon_url = '/images/icons/heroku.png'

    def get_status(self):
        r = requests.get('https://status.heroku.com/api/v3/current-status')
        res = r.json()
        status = res['status']['Production']

        if status == 'green':
            return Status.ok
        elif status == 'yellow':
            return Status.minor
        elif status == 'orange':
            return Status.major
        elif status == 'red':
            return Status.critical
