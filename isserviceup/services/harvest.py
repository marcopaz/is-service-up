from isserviceup.services.models.statuspage import StatusPagePlugin


class Harvest(StatusPagePlugin):
    name = 'Harvest'
    status_url = 'http://www.harveststatus.com'
    icon_url = '/images/icons/harvest.png'
