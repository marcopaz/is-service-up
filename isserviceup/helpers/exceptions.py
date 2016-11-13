from flask import jsonify
from werkzeug.exceptions import HTTPException


class ApiException(Exception):
    def __init__(self, message, status_code=400, **kwargs):
        super(ApiException, self).__init__()
        self.message = message
        self.status_code = status_code
        self.extra = kwargs


def format_exception(message, code=None, extra=None):
    res = {
        'status': 'error',
        'error': message or 'server error',
        'code': code,
    }
    if extra is not None:
        res.update(extra)
    return res


def handle_exception(error):
    code = 500
    message = None
    if hasattr(error, 'status_code') :
        code = error.status_code
    if hasattr(error, 'message') :
        message = str(error.message)
    if isinstance(error, HTTPException):
        code = error.code
        message = str(error)

    extra = error.extra if hasattr(error, 'extra') else None

    response = jsonify(format_exception(message, code=code, extra=extra))
    response.status_code = code
    return response
