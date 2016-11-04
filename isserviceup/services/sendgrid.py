from isserviceup.services.models.statuspage import StatusPagePlugin


class SendGrid(StatusPagePlugin):
    name = 'SendGrid'
    status_url = 'http://status.sendgrid.com/'
    icon_url = '/images/icons/sendgrid.png'
