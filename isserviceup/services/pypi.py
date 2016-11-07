from isserviceup.services.models.statuspage import StatusPagePlugin


class PythonInfra(StatusPagePlugin):
    name = 'Python Infrastructure'
    status_url = 'https://status.python.org/'
    icon_url = '/images/icons/pyinfra.png'
