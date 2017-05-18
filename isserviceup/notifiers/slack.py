import requests
from isserviceup.notifiers.notifier import Notifier


class Slack(Notifier):

    def __init__(self, web_hook_url):
        self.web_hook_url = web_hook_url

    def _build_payload(self, service, old_status, new_status):
        from isserviceup.config import config
        host_url = config.FRONTEND_URL
        if host_url[-1] == '/':
            host_url = host_url[:-1]
        payload = {
            "username": "IsServiceUp.com",
            "icon_url": '{}{}'.format(host_url, service.icon_url),
            "text": "{}'s new status is <{}|{}> (was {})".format(
                service.name,
                service.status_url,
                new_status,
                old_status,
            )
        }
        return payload

    def notify(self, service, old_status, new_status):
        payload = self._build_payload(service, old_status, new_status)
        requests.post(self.web_hook_url, json=payload)


if __name__ == '__main__':
    pass
