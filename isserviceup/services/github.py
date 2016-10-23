import requests

from isserviceup.services.models.service import Service, Status


class Heroku(Service):
    name = 'Heroku'
    status_url = 'https://status.heroku.com/'
    icon_url = '/images/icons/heroku.png'

    def get_status(self):
        r = requests.get('https://status.heroku.com/api/ui/systems?include=open-incidents.tags%2Copen-incidents.current-update.service-statuses')
        if r.status_code != 200:
            return Status.critical

        res = r.json()
        is_down = any(x['relationships']['open-incidents']['data'] for x in res['data'])

        if is_down:
            return Status.critical
        else:
            return Status.ok
