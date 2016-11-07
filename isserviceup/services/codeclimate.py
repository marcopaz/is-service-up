from isserviceup.services.models.statuspage import StatusPagePlugin


class CodeClimate(StatusPagePlugin):
    name = 'Code Climate'
    status_url = 'http://status.codeclimate.com/'
    icon_url = '/images/icons/codeclimate.png'
