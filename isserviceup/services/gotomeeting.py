from isserviceup.services.models.statuspage import StatusPagePlugin


class GotoMeeting(StatusPagePlugin):
    name = 'GoToMeeting'
    status_url = 'http://status.gotomeeting.com/'
    icon_url = '/images/icons/gotomeeting.png'
