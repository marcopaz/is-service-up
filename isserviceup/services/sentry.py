from isserviceup.services.models.statuspage import StatusPagePlugin


class Sentry(StatusPagePlugin):
    name = 'Sentry'
    status_url = 'https://status.sentry.io/'
    icon_url = '/images/icons/sentry.png'
