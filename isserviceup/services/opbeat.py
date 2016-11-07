from isserviceup.services.models.statuspage import StatusPagePlugin


class OpBeat(StatusPagePlugin):
    name = 'opbeat'
    status_url = 'http://status.opbeat.com/'
    icon_url = '/images/icons/opbeat.png'
