import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class AWS(Service):
    name = 'Amazon Web Services'
    status_url = 'http://status.aws.amazon.com/'
    icon_url = '/images/icons/aws.png'

    def get_status(self):
        r = requests.get(self.status_url)
        if r.status_code != 200:
            return Status.unavailable

        b = BeautifulSoup(r.content, 'html.parser')
        tc = str(b.find('table'))

        if ('status0.gif' in tc) or ('status1.gif' in tc):
            return Status.ok
        elif 'status2.gif' in tc:
            return Status.minor
        elif 'status3.gif' in tc:
            return Status.critical
        else:
            raise Exception('unexpected status')
