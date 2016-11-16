from enum import Enum


class Status(Enum):
    ok = 1              # green
    maintenance = 2     # blue
    minor = 3           # yellow
    major = 4           # orange
    critical = 5        # red
    unavailable = 6     # gray


class Service(object):

    @property
    def id(self):
        return self.__class__.__name__

    @property
    def status_url(self):
        raise NotImplemented()

    @property
    def icon_url(self):
        raise NotImplemented()

    @property
    def name(self):
        raise NotImplemented()

    def get_status(self):
        raise NotImplemented()
