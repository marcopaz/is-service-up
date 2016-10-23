from datetime import timedelta

from isserviceup.config import config

BROKER_URL = config.CELERY_BROKER
BROKER_HEARTBEAT = 10

CELERY_RESULT_BACKEND = config.CELERY_BACKEND
CELERY_TASK_RESULT_EXPIRES = 1 * 3600
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_ALWAYS_EAGER = config.CELERY_EAGER
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
CELERY_ACKS_LATE = False
CELERY_ANNOTATIONS = {'*': {'max_retries': 10, 'default_retry_delay': 60}}
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_TASK_SOFT_TIME_LIMIT = 600
CELERYD_TASK_TIME_LIMIT = 1800
CELERY_ENABLE_UTC = True
CELERY_IGNORE_RESULT = True

CELERYBEAT_SCHEDULE = {
    'update-status': {
        'task': 'update-services-status',
        'schedule': timedelta(seconds=config.STATUS_UPDATE_INTERVAL),
    },
}
