import os
import stat
import shutil
from decouple import config
from isserviceup.notifiers.cachet import Cachet


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
# If True, on the first status update of the run, it will notify the status
# even if they didn't change.
NOTIFY_ON_STARTUP = config('NOTIFY_ON_STARTUP', default=False, cast=bool)

# To use, set CACHET_NOTIFIER=True, and set the values for
# CACHET_URL, CACHET_TOKEN, CACHET_COMPONENTS.
CACHET_NOTIFIER = config('CACHET_NOTIFIER', default=False, cast=bool)
if CACHET_NOTIFIER:
    NOTIFIERS.append(Cachet())

# List of services separated by comma, a service is represented by the name of
# its class. If not specified the server will fetch the status of all services
# inside the services folder.
SERVICES = config('SERVICES', cast=s2l, default=None)

# This copies the key from a location set in the PRIVATE_SSH_KEY option to the
# ~/.ssh directory. For example, you can share a key in the 'shared' directory
# and then set the option to '/home/app/shared/keyfilename' so services that
# need to connect through SSH can use it. If you are going to share it, the
# file needs to have permissions to be read by other users to be able to copy
# it. Also, remember is a PRIVATE key, so generate a new one, and give it
# the minimum pemissions needed to check if the service is up and running.
PRIVATE_SSH_KEY = config('PRIVATE_SSH_KEY', default='')


# When you need to use the SSH key, call ensure_private_ssh_key that will
# return if the key was set and properly copied in the corresponding directory.
def ensure_private_ssh_key():
    global PRIVATE_SSH_KEY
    if PRIVATE_SSH_KEY:
        key_path = os.path.expanduser('~/.ssh')
        key_file = os.path.join(key_path, 'id_rsa')
        try:
            if not os.path.isdir(key_path):
                os.mkdir(key_path)
            if not os.path.isfile(key_file):
                shutil.copyfile(PRIVATE_SSH_KEY, key_file)
                os.chmod(key_file, stat.S_IWRITE | stat.S_IREAD)
        except (IOError, OSError) as error:
            PRIVATE_SSH_KEY = ''
            print(error)
        else:
            return True
    return False


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
