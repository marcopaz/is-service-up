from isserviceup.services.models.statuspage import StatusPagePlugin


class StatusPage(StatusPagePlugin):
    name = 'StatusPage'
    status_url = 'http://metastatuspage.com/'
    icon_url = '/images/icons/statuspage.png'
