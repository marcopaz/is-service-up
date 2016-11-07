from isserviceup.services.models.statuspage import StatusPagePlugin


class DataDog(StatusPagePlugin):
    name = 'DataDog'
    status_url = 'https://status.datadoghq.com/'
    icon_url = '/images/icons/datadog.png'
