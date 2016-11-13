from flask import Blueprint
from flask import redirect
from flask import request

from isserviceup.config import config
from isserviceup.helpers import github
from isserviceup.storage import sessions
from isserviceup.storage.users import upsert_user

mod = Blueprint('auth', __name__)


@mod.route('/oauth_callback', methods=['GET'])
def oauth_callback():
    code = request.args['code']

    res = github.get_access_token(code)
    access_token = res.json()['access_token']

    res = github.get_user_info(access_token)
    data = res.json()

    user = upsert_user(github_access_token=access_token,
                       avatar_url=data['avatar_url'],
                       username=data['login'])
    print('user={}'.format(user))

    sid = sessions.create({
        'user_id': str(user.id),
    })

    return redirect(config.FRONTEND_URL + '#/?code=' + sid)
