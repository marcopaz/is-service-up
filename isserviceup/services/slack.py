import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class Slack(Service):
    name = 'Slack'
    status_url = 'https://status.slack.com/'
    icon_url = '/images/icons/slack.png'

    def get_status(self):
        r = requests.get(self.status_url)
        b = BeautifulSoup(r.content, 'html.parser')
        div = b.select_one('.current_status')

        status_classes = div.attrs['class']

        if 'all_clear' in status_classes:
            return Status.ok
        elif 'issue' in status_classes:
            return Status.major
        elif 'maintenance' in status_classes:
            return Status.maintenance
        else:
            raise Exception('unexpected status')
