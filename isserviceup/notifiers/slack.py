from decouple import config
import requests
from isserviceup.notifiers.notifier import Notifier

SLACK_WEBHOOK_URL = config('SLACK_WEBHOOK_URL', default=None)


class Slack(Notifier):

    def notify(self, service, old_status, new_status):
        payload = {
            "text": "{}'s new status is {} (was {})".format(
                service,
                new_status,
                old_status,
            )
        }
        r = requests.post(SLACK_WEBHOOK_URL, json=payload)
        print(r.status_code)
