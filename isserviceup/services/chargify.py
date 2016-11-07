from isserviceup.services.models.statuspage import StatusPagePlugin


class Chargify(StatusPagePlugin):
    name = 'Chargify'
    status_url = 'http://status.chargify.io/'
    icon_url = '/images/icons/chargify.png'
