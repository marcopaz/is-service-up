from isserviceup.services.models.statuspage import StatusPagePlugin


class PagerDuty(StatusPagePlugin):
    name = 'PagerDuty'
    status_url = 'https://status.pagerduty.com/'
    icon_url = '/images/icons/pagerduty.png'
