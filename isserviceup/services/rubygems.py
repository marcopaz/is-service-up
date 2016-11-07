from isserviceup.services.models.statuspage import StatusPagePlugin


class RubyGems(StatusPagePlugin):
    name = 'Ruby Gems'
    status_url = 'https://status.rubygems.org/'
    icon_url = '/images/icons/rubygems.png'
