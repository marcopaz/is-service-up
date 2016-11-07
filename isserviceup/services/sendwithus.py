from isserviceup.services.models.statuspage import StatusPagePlugin


class SendWithUs(StatusPagePlugin):
    name = 'Send with us'
    status_url = 'https://status.sendwithus.com/'
    icon_url = '/images/icons/sendwithus.png'
