from isserviceup.services.models.statuspage import StatusPagePlugin


class Pingdom(StatusPagePlugin):
    name = 'Pingdom'
    status_url = 'http://status.pingdom.com/'
    icon_url = '/images/icons/pingdom.png'
