from isserviceup.services.models.statuspage import StatusPagePlugin


class Twilio(StatusPagePlugin):
    name = 'Twilio'
    status_url = 'https://status.twilio.com/'
    icon_url = '/images/icons/twilio.png'
