from isserviceup.services.models.statuspage import StatusPagePlugin


class Atlassian(StatusPagePlugin):
    name = 'Atlassian'
    status_url = 'http://status.atlassian.com/'
    icon_url = '/images/icons/atlassian.png'
