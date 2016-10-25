from isserviceup.services.models.statuspage import StatusPagePlugin


class Linode(StatusPagePlugin):
    name = 'Linode'
    status_url = 'http://status.linode.com/'
    icon_url = '/images/icons/linode.png'
