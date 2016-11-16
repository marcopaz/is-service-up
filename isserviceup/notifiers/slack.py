from decouple import config
import requests
from isserviceup.notifiers.notifier import Notifier


class Slack(Notifier):

    def __init__(self, web_hook_url):
        self.web_hook_url = web_hook_url

    def notify(self, service, old_status, new_status):
        payload = {
            "username": "IsServiceUp.com",
            "icon_url": service.icon_url,
            "text": "{}'s new status is <{}|{}> (was {})".format(
                service.name,
                service.status_url,
                new_status,
                old_status,
            )
        }
        r = requests.post(self.web_hook_url, json=payload)
