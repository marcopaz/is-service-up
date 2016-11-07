from isserviceup.services.models.statuspage import StatusPagePlugin


class PackageCloud(StatusPagePlugin):
    name = 'Package Cloud'
    status_url = 'http://www.packagecloudstatus.io/'
    icon_url = '/images/icons/packagecloud.png'
