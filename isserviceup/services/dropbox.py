from isserviceup.services.models.statuspage import StatusPagePlugin


class Dropbox(StatusPagePlugin):
    name = 'Dropbox'
    status_url = 'https://status.dropbox.com'
    icon_url = '/images/icons/dropbox.png'
