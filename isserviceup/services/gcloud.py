import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class GCloud(Service):
    name = 'Google Cloud'
    status_url = 'https://status.cloud.google.com/'
    icon_url = '/images/icons/gcloud.png'

    def get_status(self):
        r = requests.get(self.status_url)
        if r.status_code != 200:
            return Status.critical

        b = BeautifulSoup(r.content, 'html.parser')
        status = next(x for x in b.find(class_='subheader').attrs['class']
                      if x.startswith('open-incident-bar-'))

        if status == 'open-incident-bar-clear':
            return Status.ok
        elif status == 'open-incident-bar-medium':
            return Status.major
        elif status == 'open-incident-bar-high':
            return Status.critical
        else:
            raise Exception('unexpected status')
