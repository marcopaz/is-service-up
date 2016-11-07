from isserviceup.services.models.statuspage import StatusPagePlugin


class BitBucket(StatusPagePlugin):
    name = 'BitBucket'
    status_url = 'https://status.bitbucket.org/'
    icon_url = '/images/icons/bitbucket.png'
