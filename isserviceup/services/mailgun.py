from isserviceup.services.models.statuspage import StatusPagePlugin


class MailGun(StatusPagePlugin):
    name = 'MailGun'
    status_url = 'http://status.mailgun.com/'
    icon_url = '/images/icons/mailgun.png'
