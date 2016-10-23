import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class StatusPagePlugin(Service):

    def get_status(self):
        r = requests.get(self.status_url)
        if r.status_code != 200:
            return Status.unavailable

        b = BeautifulSoup(r.content, 'html.parser')

        page_status = b.find(class_='page-status')

        if page_status is None:
            if b.find(class_='unresolved-incidents'):
                return Status.major

        status = next(x for x in page_status.attrs['class'] if x.startswith('status-'))

        if status == 'status-none':
            return Status.ok
        elif status == 'status-critical':
            return Status.critical
        elif status == 'status-major':
            return Status.major
        elif status == 'status-minor':
            return Status.minor
        elif status == 'status-maintenance':
            return Status.maintenance
        else:
            raise Exception('unexpected status')