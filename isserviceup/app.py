import logging
import datetime

from flask_cors import CORS

from isserviceup.storage.services import get_status as get_services_status
from isserviceup.config import config
from flask import Flask, jsonify, render_template
from raven.contrib.flask import Sentry
import redis

from isserviceup.services.models.service import Status

app = Flask(__name__, static_url_path='', static_folder='../frontend/dist')
app.config.from_object(config)
app.debug = config.DEBUG
CORS(app)

if config.SENTRY_DSN:
    sentry = Sentry(app, logging=True, level=logging.ERROR)
rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)


def format_services_status(services, values, last_update):
    data = []
    for i, service in enumerate(services):
        status = values[i] if values[i] else Status.unavailable
        s = {
            'name': service.name,
            'icon_url': service.icon_url,
            'status_url': service.status_url,
            'status': status.name,
        }
        data.append(s)

    if last_update:
        now = datetime.datetime.now()
        last_update = int((now - last_update).total_seconds())

    return data, last_update


def services_status():
    services = config.SERVICES
    values, last_update = get_services_status(rclient, services)
    return format_services_status(services, values, last_update)


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/status', methods=['GET'])
def status():
    services, last_update = services_status()
    return jsonify({
        'data': {
            'services': services,
            'last_update': last_update,
        }
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
