from isserviceup.services.models.statuspage import StatusPagePlugin


class Dnsimple(StatusPagePlugin):
    name = 'dnsimple'
    status_url = 'http://dnsimplestatus.com/'
    icon_url = '/images/icons/dnsimple.png'
