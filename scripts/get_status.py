#!/usr/bin/env python
from isserviceup.config import config

for service in config.SERVICES:
    print('{}: {}'.format(service.name, service.get_status().name))
