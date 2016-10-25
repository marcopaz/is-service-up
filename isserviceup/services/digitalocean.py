import requests
from bs4 import BeautifulSoup

from isserviceup.services.models.service import Service, Status


class DO():
    name = 'DigitalOcean'
    status_url = 'https://status.digitalocean.com'
    icon_url = '/images/icons/do.png'

    def get_status(self):
        r = requests.get(self.status_url)
        if r.status_code != 200:
            return Status.unavailable

        b = BeautifulSoup(r.content, 'html.parser')
        div = str(b.findAll("div", { "class" : "lrg"}))
        if 'success' in div:
            return Status.ok
        elif 'interim' in div:
            return Status.minor
        elif 'alert' in div:
            return Status.critical
        else:
            raise Exception('unexpected status')
