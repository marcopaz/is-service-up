from isserviceup.services.models.statuspage import StatusPagePlugin


class SparkPost(StatusPagePlugin):
    name = 'SparkPost'
    status_url = 'http://status.sparkpost.com/'
    icon_url = '/images/icons/sparkpost.png'
