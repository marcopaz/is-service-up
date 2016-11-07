from isserviceup.services.models.statuspage import StatusPagePlugin


class HashiCorp(StatusPagePlugin):
    name = 'HashiCorp'
    status_url = 'https://status.hashicorp.com/'
    icon_url = '/images/icons/hashicorp.png'
