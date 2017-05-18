import requests
from enum import Enum
from decouple import config
from isserviceup.notifiers.notifier import Notifier


class CachetStatus(Enum):
    ok = 1
    minor = 2
    major = 3
    critical = 4

    @staticmethod
    def get_cachet_status(status):
        from isserviceup.services.models.service import Status
        status_map = {
            Status.ok: CachetStatus.ok,
            Status.maintenance: CachetStatus.minor,
            Status.minor: CachetStatus.minor,
            Status.major: CachetStatus.major,
            Status.critical: CachetStatus.critical,
            Status.unavailable: CachetStatus.critical,
        }
        status = status and Status[status]
        return (status_map[status].value if status in status_map
                else CachetStatus.critical.value)


class Cachet(Notifier):
    """Notifies to the Cachet status page components, about the state of their
    corresponding services.

    :param cachet_url: The URL for the Cachet status page.
        If empty, will get it from config('CACHET_URL').
    :type cachet: str
    :param cachet_token: The Cachet API Token.
        If empty, will get it from config('CACHET_TOKEN').
    :type cachet_token: str
    :param cachet_components: Which components in Cachet are going to be
        notified. Is a dictionary with each key being the service class, and
        its value, the Cachet component id. If empty, will get it from
        config('CACHET_COMPONENTS'), and it has to be a comma separated string
        with each service class, a colon, and the component id. (For example,
        CACHET_COMPONENTS=Docker:1,Github:4)
    :type cachet_components: dict
    """

    def __init__(self, cachet_url="", cachet_token="",
                 cachet_components=None):
        self.cachet_url = cachet_url or config('CACHET_URL', default=None)
        self.cachet_token = (cachet_token or
                             config('CACHET_TOKEN', default=None))
        self.cachet_components = (cachet_components or
                                  config('CACHET_COMPONENTS', default=None,
                                         cast=self._components_to_dict))

    def _components_to_dict(self, components=None):
        try:
            return dict([[side.strip() for side in component.split(":")]
                         for component in components.split(",")])
        except ValueError as error:
            print("Value error: {msg}".format(msg=error.message))
            return {}

    def _get_component_name(self, service):
        return type(service).__name__

    def _get_component_url(self, service):
        component = self._get_component_name(service)
        if component in self.cachet_components:
            url = "{base_url}/api/v1/components/{component}".format(
                base_url=self.cachet_url.strip("/"),
                component=self.cachet_components[component]
            )
            return url
        return False

    def _get_headers(self):
        return {
            'Content-Type': 'application/json',
            'X-Cachet-Token': self.cachet_token,
        }

    def _build_payload(self, service, old_status, new_status):
        payload = {
            'name': service.name,
            'status': CachetStatus.get_cachet_status(new_status),
            'old_status': CachetStatus.get_cachet_status(old_status),
        }
        return payload

    def _is_valid(self, service):
        return (
            self.cachet_url and self.cachet_token and self.cachet_components
            and self._get_component_name(service) in self.cachet_components
        )

    def notify(self, service, old_status, new_status):
        if self._is_valid(service):
            url = self._get_component_url(service)
            headers = self._get_headers()
            payload = self._build_payload(service, old_status, new_status)
            print("Notifying {} with {}".format(url, payload))
            requests.put(url, json=payload, headers=headers)
