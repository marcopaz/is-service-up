import logging
import datetime

from isserviceup.storage.services import get_status as get_services_status
from isserviceup.config import config
from flask import Flask, jsonify, render_template
from raven.contrib.flask import Sentry
import redis

from isserviceup.services.models.service import Status

app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object(config)
app.debug = config.DEBUG

if config.SENTRY_DSN:
    sentry = Sentry(app, logging=True, level=logging.ERROR)
rclient = redis.from_url(config.REDIS_URL, charset="utf-8", decode_responses=True)


def format_services_status(services, values, last_update):
    status_values = {
        Status.ok: ('Operational', 'fa-check', 'green'),
        Status.minor: ('Degraded Performance', 'fa-minus-square', 'yellow'),
        Status.major: ('Partial Outage', 'fa-exclamation-triangle', 'orange'),
        Status.critical: ('Major Outage', 'fa-times', 'red'),
        Status.maintenance: ('Maintenance', 'fa-wrench', 'blue'),
        Status.unavailable: ('Status Unavailable', 'fa-question', 'gray')
    }

    data = []
    for i, service in enumerate(services):
        status = values[i] if values[i] else Status.unavailable
        s = {
            'name': service.name,
            'status_page_url': service.status_url,
            'icon_url': service.icon_url,
            'status': status.name,
            'status_human': status_values[status][0],
            'status_icon': status_values[status][1],
            'status_color': status_values[status][2],
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
    services, last_update = services_status()
    return render_template('index.html', services=services, last_update=last_update)


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
