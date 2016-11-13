from flask import request
from six import wraps

from isserviceup.helpers.exceptions import ApiException
from isserviceup.storage import sessions


def authenticated(blocking=True):

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = None
            auth = request.headers.get('Authorization')
            if auth and len(auth) >= 7:
                sid = auth[7:]  # 'Bearer ' prefix
                user = sessions.get(sid)
            if blocking and not user:
                raise ApiException('unauthorized', status_code=401)
            res = f(user=user, *args, **kwargs)
            return res
        return wrapper

    return decorator
