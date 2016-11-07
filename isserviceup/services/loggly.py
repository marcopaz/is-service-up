from isserviceup.services.models.statuspage import StatusPagePlugin


class Loggly(StatusPagePlugin):
    name = 'Loggly'
    status_url = 'http://status.loggly.com//'
    icon_url = '/images/icons/loggly.jpg'
