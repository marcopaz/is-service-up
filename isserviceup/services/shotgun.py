from isserviceup.services.models.statuspage import StatusPagePlugin


class Shotgun(StatusPagePlugin):
    name = 'Shotgun'
    status_url = 'http://status.shotgunsoftware.com/'
    icon_url = '/images/icons/shotgun.png'
