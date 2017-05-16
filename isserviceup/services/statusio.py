from isserviceup.services.models.statusio import StatusIOPlugin


class StatusIO(StatusIOPlugin):
    name = 'Status.io'
    status_url = 'https://status.status.io/'
    statuspage_id = '51f6f2088643809b7200000d'
    icon_url = '/images/icons/statusio.png'
