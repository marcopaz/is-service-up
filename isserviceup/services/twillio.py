from isserviceup.services.models.statuspage import StatusPagePlugin


class Twillio(StatusPagePlugin):
    name = 'Twillio'
    status_url = 'https://status.twilio.com/'
    icon_url = '/images/icons/twillio.png'
