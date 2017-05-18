import requests
import subprocess
from decouple import config
from isserviceup.config import config as isu_config
from isserviceup.services.models.service import Service, Status
try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse


class GitLabPlugin(Service):

    icon_url = '/images/icons/gitlab.png'

    def __init__(self):
        # Will check if the GitLab website is OK.
        self.check_http = config('GITLAB_CHECK_HTTP', default=True, cast=bool)
        # Will check if the GitLab JSON API is OK.
        self.check_json = config('GITLAB_CHECK_JSON', default=True, cast=bool)
        # Will check if the SSH connections to git@{gitlab_url} are OK.
        # To use this you need to set the PRIVATE_SSH_KEY option in the config.
        self.check_ssh = config('GITLAB_CHECK_SSH', default=False, cast=bool)
        # If you need to monitor multiple GitLab instances and need each one to
        # have a different behaviour: extend this class, override the __init__
        # function, call super, and then override these properties.

    def _check_http(self):
        request = requests.get(self.status_url)
        return request.ok

    def _check_json(self):
        request = requests.get('{base}/api/v4/projects'.format(
            base=self.status_url.strip('/')
        ))
        try:
            if request.json():
                return True
        except ValueError as error:
            print('Value error: {msg}'.format(msg=error.message))
        return False

    def _check_private_ssh_key(self):
        if not isu_config.ensure_private_ssh_key():
            print('GitLab SSH error for {url}: {error}'.format(
                url=self.status_url,
                error='No private SSH key found. Make sure the file path you '
                      'set in option PRIVATE_SSH_KEY is correct. If it is a '
                      'shared file, make sure it has permissions to be read '
                      'by other users.'))
            return False
        return True

    def _check_ssh(self):
        if not self._check_private_ssh_key():
            return False
        url = urlparse(self.status_url)
        try:
            ssh = subprocess.check_output([
                'ssh', '-T', '-o StrictHostKeyChecking=no',
                'git@{host}'.format(host=url.netloc)
            ])
        except subprocess.CalledProcessError as error:
            print('GitLab SSH error for {url}: {error}'.format(
                url=self.status_url, error=error))
            return False
        return 'Welcome to GitLab' in str(ssh)

    def get_status(self):
        status = [
            not self.check_http or self._check_http(),
            not self.check_json or self._check_json(),
            not self.check_ssh or self._check_ssh(),
        ]
        if all(status):
            return Status.ok
        elif any(status):
            return Status.major
        return Status.critical
