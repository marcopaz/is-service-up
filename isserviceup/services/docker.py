from isserviceup.services.models.statusio import StatusIOPlugin


class Docker(StatusIOPlugin):
    name = 'Docker'
    status_url = 'https://status.docker.com/'
    statuspage_id = '533c6539221ae15e3f000031'
    icon_url = '/images/icons/docker.png'
