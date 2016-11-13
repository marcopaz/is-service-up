from flask import Blueprint, jsonify

from isserviceup import managers
from isserviceup.config import config
from isserviceup.services import SERVICES
from isserviceup.services.models.service import Status
from isserviceup.storage.services import get_status as get_services_status

mod = Blueprint('status', __name__)


@mod.route('', methods=['GET'])
def status():
    services = SERVICES.values()
    values = get_services_status(managers.rclient, services)

    data = []
    for i, service in enumerate(services):
        status = values[i] if values[i] else Status.unavailable
        s = {
            'name': service.name,
            'icon_url': service.icon_url,
            'status_url': service.status_url,
            'status': status.name,
            'id': service.id,
        }
        data.append(s)

    return jsonify({
        'data': {
            'services': data,
        }
    })
