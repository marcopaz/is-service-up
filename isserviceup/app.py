import logging

import traceback
from flask import Flask
from flask_cors import CORS
from raven.contrib.flask import Sentry

from isserviceup.config import config
from isserviceup.api import status as status_bp

app = Flask(__name__, static_url_path='', static_folder='../frontend/dist')
app.config.from_object(config)
app.debug = config.DEBUG
CORS(app)

sentry = None
if config.SENTRY_DSN:
    sentry = Sentry(app, logging=True, level=logging.ERROR)


app.register_blueprint(status_bp.mod, url_prefix='/status')


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
