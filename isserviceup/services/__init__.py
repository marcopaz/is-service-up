from isserviceup.config import config
import importlib
import inspect
import os
import re
from isserviceup.services.models.service import Service
import sys
current_module = sys.modules[__name__]


def load_services():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    pluginfiles = [x for x in os.listdir(os.path.dirname(__file__)) if pysearchre.search(x)]
    form_module = lambda fp: '.' + os.path.splitext(fp)[0]
    plugins = map(form_module, pluginfiles)
    modules = []
    for plugin in plugins:
        if not plugin.startswith('.__'):
            modules.append(importlib.import_module(plugin, package=current_module.__name__))

    services = {}
    for module in modules:
        for item_name in dir(module):
            item = getattr(module, item_name)
            if inspect.isclass(item) and issubclass(item, Service) and isinstance(item.name, str):
                service_id = item.__name__
                if config.SERVICES is not None and service_id not in config.SERVICES:
                    continue
                if item.name in services:
                    raise Exception('found multiple service with the name "{}"'.format(item.name))
                services[service_id] = item()
    return services

SERVICES = load_services()


if __name__ == '__main__':
    print(SERVICES)
