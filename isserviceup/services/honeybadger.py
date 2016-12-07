from isserviceup.services.models.statuspage import StatusPagePlugin


class Honeybadger(StatusPagePlugin):
    name = 'Honeybadger'
    status_url = 'http://status.honeybadger.io/'
    icon_url = '/images/icons/honeybadger.png'
