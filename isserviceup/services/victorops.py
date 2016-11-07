from isserviceup.services.models.statuspage import StatusPagePlugin


class VictorOps(StatusPagePlugin):
    name = 'VictorOps'
    status_url = 'http://victorops.statuspage.io/'
    icon_url = '/images/icons/victorops.png'
