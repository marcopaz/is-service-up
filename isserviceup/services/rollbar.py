from isserviceup.services.models.statuspage import StatusPagePlugin


class RollBar(StatusPagePlugin):
    name = 'RollBar'
    status_url = 'http://status.rollbar.com/'
    icon_url = '/images/icons/rollbar.png'
