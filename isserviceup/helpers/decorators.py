from flask import request
from six import wraps

from isserviceup.helpers.exceptions import ApiException
from isserviceup.storage import sessions
from isserviceup.storage.users import get_user


def authenticated(blocking=True):

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = None
            auth = request.headers.get('Authorization')
            if auth and len(auth) >= 7:
                sid = auth[7:]  # 'Bearer ' prefix
                session = sessions.get(sid)
                if session and session.get('user_id'):
                    user = get_user(session['user_id'])
                    if user:
                        user.sid = sid
            if blocking and not user:
                raise ApiException('unauthorized', status_code=401)
            res = f(user=user, *args, **kwargs)
            return res
        return wrapper

    return decorator
