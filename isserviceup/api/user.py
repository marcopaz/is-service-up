from flask import Blueprint, jsonify
from flask import request

from isserviceup.helpers.decorators import authenticated
from isserviceup.helpers.exceptions import ApiException
from isserviceup.services import SERVICES
from isserviceup.storage import sessions
from isserviceup.storage.favorites import update_favorite_status

mod = Blueprint('user', __name__)


@mod.route('', methods=['GET'])
@authenticated()
def get_user(user):
    return jsonify(user.as_dict())


@mod.route('', methods=['POST'])
@authenticated()
def edit_user(user):
    data = request.json
    try:
        user.edit(data)
    except ValueError:
        raise ApiException('bad request', 400)
    return jsonify(user.as_dict())


@mod.route('/logout', methods=['GET'])
@authenticated(blocking=False)
def logout(user):
    if user:
        sessions.destroy(user.sid)
    return jsonify({
        'status': 'ok',
    })


@mod.route('/favorite', methods=['POST'])
@authenticated()
def star(user):
    data = request.json

    if not data or data.get('service_id') is None or data.get('status') is None:
        raise ApiException('bad request', 400)

    service_id = data['service_id']
    status = data['status']

    try:
        SERVICES[service_id]
    except Exception:
        raise ApiException('bad request', 400)

    update_favorite_status(str(user.id), service_id, status)

    return jsonify({
        'status': 'ok',
    })
