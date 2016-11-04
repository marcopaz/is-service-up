from isserviceup.services.models.statuspage import StatusPagePlugin


class Quay(StatusPagePlugin):
    name = 'Quay'
    status_url = 'http://status.quay.io/'
    icon_url = '/images/icons/quay.png'
