from isserviceup.services.models.statuspage import StatusPagePlugin


class FTrack(StatusPagePlugin):
    name = 'FTrack'
    status_url = 'http://status.ftrack.com/'
    icon_url = '/images/icons/ftrack.png'
