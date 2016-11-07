from isserviceup.services.models.statuspage import StatusPagePlugin


class Box(StatusPagePlugin):
    name = 'Box'
    status_url = 'https://status.box.com/'
    icon_url = '/images/icons/box.png'
