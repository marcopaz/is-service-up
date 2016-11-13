import json

from isserviceup import managers
from isserviceup.helpers import utils


SESSION_TTL = 60*60*24*30
_session_key = lambda x: 'session:{}'.format(x)


def get(sid):
    res = managers.rclient.get(_session_key(sid))
    if not res:
        return None
    res = json.loads(res)
    return res


def create(data):
    sid = utils.random_string(16)
    data['sid'] = sid
    managers.rclient.set(_session_key(sid), json.dumps(data), ex=SESSION_TTL)
    return sid


def destroy(sid):
    managers.rclient.delete(_session_key(sid))
    return True
