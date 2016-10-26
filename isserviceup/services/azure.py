import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class Azure(Service):
    name = 'Microsoft Azure'
    status_url = 'https://azure.microsoft.com/en-us/status/'
    icon_url = '/images/icons/azure.png'

    def get_status(self):
        r = requests.get(self.status_url)
        b = BeautifulSoup(r.content, 'html.parser')
        div = str(b.select_one('.section.section-size3.section-slate09'))

        if 'health-circle' in div or 'health-check' in div:
            return Status.ok
        elif 'health-warning' in div:
            return Status.minor
        elif 'health-error' in div:
            return Status.critical
        else:
            raise Exception('unexpected status')
