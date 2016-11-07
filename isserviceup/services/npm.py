from isserviceup.services.models.statuspage import StatusPagePlugin


class NPM(StatusPagePlugin):
    name = 'NPM'
    status_url = 'http://status.npmjs.org/'
    icon_url = '/images/icons/npm.png'
