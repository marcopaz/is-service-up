import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class Stripe(Service):
    name = 'Stripe'
    status_url = 'https://status.stripe.com/'
    icon_url = '/images/icons/stripe.png'

    def get_status(self):
        r = requests.get(self.status_url)
        b = BeautifulSoup(r.content, 'html.parser')
        div = b.select_one('.status-bubble')

        status_classes = div.attrs['class']

        if 'status-up' in status_classes:
            return Status.ok
        elif 'status-down' in status_classes:
            return Status.critical
        else:
            raise Exception('unexpected status')
