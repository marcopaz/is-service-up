from isserviceup.services.models.statuspage import StatusPagePlugin


class GoCardless(StatusPagePlugin):
    name = 'Go Cardless'
    status_url = 'https://www.gocardless-status.com/'
    icon_url = '/images/icons/gocardless.png'
