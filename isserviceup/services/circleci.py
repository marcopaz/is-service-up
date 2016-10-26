from isserviceup.services.models.statuspage import StatusPagePlugin


class CircleCI(StatusPagePlugin):
    name = 'CircleCI'
    status_url = 'https://status.circleci.com/'
    icon_url = '/images/icons/circleci.png'
