from isserviceup.services.models.statuspage import StatusPagePlugin


class PingIdentity(StatusPagePlugin):
    name = 'Ping Identity'
    status_url = 'https://status.pingidentity.com/'
    icon_url = '/images/icons/pingidentity.png'
