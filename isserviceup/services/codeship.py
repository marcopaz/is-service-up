from isserviceup.services.models.statuspage import StatusPagePlugin


class CodeShip(StatusPagePlugin):
    name = 'Codeship'
    status_url = 'http://codeshipstatus.com/'
    icon_url = '/images/icons/codeship.png'
