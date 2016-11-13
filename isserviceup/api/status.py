from flask import Blueprint, jsonify
from flask import request

from isserviceup import managers
from isserviceup.helpers.decorators import authenticated
from isserviceup.services import SERVICES
from isserviceup.services.models.service import Status
from isserviceup.storage.favorites import get_favorite_services
from isserviceup.storage.services import get_status as get_services_status

mod = Blueprint('status', __name__)


@mod.route('', methods=['GET'])
@authenticated(blocking=False)
def status(user):
    type = request.args.get('type')
    favorite_services = []

    services = SERVICES.values()

    if user:
        favorite_services = get_favorite_services(str(user.id))

    if type == 'favorite':
        services = favorite_services
        for service in services:
            service.star = True
    else:
        favorite_services = {x.name: True for x in favorite_services}

    values = get_services_status(managers.rclient, services)

    data = []
    for i, service in enumerate(services):
        status = values[i] if values[i] else Status.unavailable
        star = True if type == 'favorite' else (service.name in favorite_services)
        s = {
            'name': service.name,
            'icon_url': service.icon_url,
            'status_url': service.status_url,
            'status': status.name,
            'star': star,
            'id': service.id,
        }
        data.append(s)

    return jsonify({
        'data': {
            'services': data,
        }
    })
