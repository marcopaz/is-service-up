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
@authenticated()
def logout(user):
    return sessions.destroy(user['sid'])
