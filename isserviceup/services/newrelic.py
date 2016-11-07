from isserviceup.services.models.statuspage import StatusPagePlugin


class NewRelic(StatusPagePlugin):
    name = 'New Relic'
    status_url = 'https://status.newrelic.com/'
    icon_url = '/images/icons/newrelic.png'
