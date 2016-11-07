from isserviceup.services.models.statuspage import StatusPagePlugin


class AuthorizeDotNet(StatusPagePlugin):
    name = 'Authorize.net'
    status_url = 'https://status.authorize.net/'
    icon_url = '/images/icons/authorizedotnet.jpg'
