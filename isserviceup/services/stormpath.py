from isserviceup.services.models.statuspage import StatusPagePlugin


class StormPath(StatusPagePlugin):
    name = 'StormPath'
    status_url = 'https://status.stormpath.com/'
    icon_url = '/images/icons/stormpath.png'
