from isserviceup.services.models.statuspage import StatusPagePlugin


class Dyn(StatusPagePlugin):
    name = 'Dyn'
    status_url = 'https://www.dynstatus.com/'
    icon_url = '/images/icons/dyn.png'
