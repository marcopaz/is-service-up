from isserviceup.services.models.statuspage import StatusPagePlugin


class Pusher(StatusPagePlugin):
    name = 'Pusher'
    status_url = 'https://status.pusher.com/'
    icon_url = '/images/icons/pusher.png'
