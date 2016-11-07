from isserviceup.services.models.statuspage import StatusPagePlugin


class Duo(StatusPagePlugin):
    name = 'Duo'
    status_url = 'https://status.duo.com/'
    icon_url = '/images/icons/duo.png'
