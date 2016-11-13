from flask import Blueprint, jsonify

from isserviceup.helpers.decorators import authenticated
from isserviceup.storage import sessions

mod = Blueprint('user', __name__)


@mod.route('', methods=['GET'])
@authenticated()
def get_user(user):
    return jsonify({
        'username': user['username'],
        'avatar_url': user['avatar_url'],
    })


@mod.route('/logout', methods=['GET'])
@authenticated(blocking=False)
def logout(user):
    if user:
        sessions.destroy(user['sid'])
    return jsonify({
        'status': 'ok',
    })
