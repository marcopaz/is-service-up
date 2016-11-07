from isserviceup.services.models.statuspage import StatusPagePlugin


class Disqus(StatusPagePlugin):
    name = 'Disqus'
    status_url = 'https://status.disqus.com/'
    icon_url = '/images/icons/disqus.png'
