import requests

from isserviceup.services.models.service import Service, Status

GitHubStatusMap = {
    'good': Status.ok,
    'major': Status.major,
    'minor': Status.minor
}


class GitHub(Service):
    name = 'GitHub'
    status_url = 'https://status.github.com/'
    icon_url = '/images/icons/github.png'

    def get_status(self):
        r = requests.get(self.status_url + 'api/status.json')
        if r.status_code != 200:
            return Status.critical

        res = r.json()
        status = res['status']

        return GitHubStatusMap[status]
