from isserviceup.services.models.statuspage import StatusPagePlugin


class Cloudflare(StatusPagePlugin):
    name = 'Cloudflare'
    status_url = 'http://www.cloudflarestatus.com/'
    icon_url = '/images/icons/cloudflare.png'
