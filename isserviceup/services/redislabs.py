from isserviceup.services.models.statuspage import StatusPagePlugin


class RedisLabs(StatusPagePlugin):
    name = 'RedisLabs'
    status_url = 'https://status.redislabs.com/'
    icon_url = '/images/icons/redislabs.png'
