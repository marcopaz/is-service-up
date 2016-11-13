import logging

import traceback
from flask import Flask
from flask_cors import CORS
from raven.contrib.flask import Sentry

from isserviceup.config import config
from isserviceup.api import status as status_bp
from isserviceup.api import auth as auth_bp
from isserviceup.helpers import exceptions

app = Flask(__name__, static_url_path='', static_folder='../frontend/dist')
app.config.from_object(config)
app.debug = config.DEBUG
CORS(app)

sentry = None
if config.SENTRY_DSN:
    sentry = Sentry(app, logging=True, level=logging.ERROR)


@app.errorhandler(Exception)
def handle_generic_exception(error):
    print('Exception={}'.format(error))
    traceback.print_exc()

    if sentry:
        sentry.captureException()

    return exceptions.handle_exception(error)


app.register_blueprint(status_bp.mod, url_prefix='/status')
app.register_blueprint(auth_bp.mod, url_prefix='/auth')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
