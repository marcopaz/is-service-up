from decouple import config
from isserviceup.services.models.gitlab import GitLabPlugin


class GitLab(GitLabPlugin):

    name = config('GITLAB_SERVICE_NAME', default='GitLab')
    status_url = config('GITLAB_URL', default='https://gitlab.com/')
