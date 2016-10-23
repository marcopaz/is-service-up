from isserviceup.services.models.statuspage import StatusPagePlugin


class Compose(StatusPagePlugin):
    name = 'Compose'
    status_url = 'https://status.compose.com/'
    icon_url = '/images/icons/compose.png'
