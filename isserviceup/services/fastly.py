from isserviceup.services.models.statuspage import StatusPagePlugin


class Fastly(StatusPagePlugin):
    name = 'Fastly'
    status_url = 'https://status.fastly.com/'
    icon_url = '/images/icons/fastly.png'
