from isserviceup.services.models.statuspage import StatusPagePlugin


class CodeShip(StatusPagePlugin):
    name = 'Code Ship'
    status_url = 'http://codeshipstatus.com/'
    icon_url = '/images/icons/codeship.png'
