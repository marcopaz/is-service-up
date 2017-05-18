from isserviceup.services.models.statuspage import StatusPagePlugin


class DigitalOcean(StatusPagePlugin):
    name = 'DigitalOcean'
    status_url = 'https://status.digitalocean.com'
    icon_url = '/images/icons/do.png'
