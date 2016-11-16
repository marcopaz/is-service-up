from decouple import config


def s2l(x):
    return [y.strip() for y in x.split(',')] if x else None


DEBUG = config('DEBUG', cast=bool, default=False)
FRONTEND_URL = config('FRONTEND_URL', default='http://localhost:8000/')
REDIS_URL = config('REDIS_URL', default='redis://redis:devpassword@redis')
MONGO_URL = config('MONGO_URL', default='mongodb://mongo/isserviceup')
STATUS_UPDATE_INTERVAL = config('STATUS_UPDATE_INTERVAL', cast=int, default=30)

SERVE_STATIC_FILES = config('SERVE_STATIC_FILES', cast=bool, default=True)

SENTRY_DSN = config('SENTRY_DSN', default=None)

CELERY_EAGER = config('CELERY_EAGER', cast=bool, default=False)
CELERY_BROKER = config('CELERY_BROKER', default=REDIS_URL)
CELERY_BACKEND = config('CELERY_BACKEND', default=REDIS_URL)

GITHUB_CLIENT_ID = config('GITHUB_CLIENT_ID', default=None)
GITHUB_CLIENT_SECRET = config('GITHUB_CLIENT_SECRET', default=None)

SLACK_WEB_HOOK_URL = config('SLACK_WEB_HOOK_URL', default=None)

NOTIFIERS = [
    # Slack(SLACK_WEB_HOOK_URL)
]

# List of services separated by comma, a service is represented by the name of its class
# if not specified the server will fetch the status of all services inside the services folder
SERVICES = config('SERVICES', cast=s2l, default=None)


# TODO: unify with frontend config
def get_status_description():
    from isserviceup.services.models.service import Status
    return {
        Status.ok: 'Operational',
        Status.minor: 'Minor Outage',
        Status.major: 'Major Outage',
        Status.critical: 'Critical Outage',
        Status.maintenance: 'Maintenance',
        Status.unavailable: 'Status Unavailable',
    }
