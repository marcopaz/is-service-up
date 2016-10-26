from isserviceup.services.models.statuspage import StatusPagePlugin


class Travis(StatusPagePlugin):
    name = 'Travis'
    status_url = 'https://www.traviscistatus.com/'
    icon_url = '/images/icons/travis.png'
