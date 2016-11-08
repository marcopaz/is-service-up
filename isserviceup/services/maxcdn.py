from isserviceup.services.models.statuspage import StatusPagePlugin


class MaxCDN(StatusPagePlugin):
    name = 'MaxCDN'
    status_url = 'https://status.maxcdn.com/'
    icon_url = '/images/icons/maxcdn.png'
