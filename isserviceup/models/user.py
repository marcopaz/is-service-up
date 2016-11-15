import datetime
from mongoengine import StringField, Document, DateTimeField, BooleanField, ListField, URLField

from isserviceup.models.favorite import Favorite
from isserviceup.services.models.service import Status

DEFAULT_MONITORED_STATUS = [
    Status.ok.name,
    Status.major.name,
    Status.critical.name
]


class User(Document):
    username = StringField(required=True, unique=True)
    avatar_url = StringField()
    github_access_token = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    monitored_status = ListField(StringField(), default=DEFAULT_MONITORED_STATUS)
    slack_webhook = URLField(default=None)

    def update_favs(self, field, value):
        Favorite.objects(user_id=str(self.id))\
            .update(**{'set__{}'.format(field): value})

    def edit(self, data):
        value = data.get('monitored_status')
        if value is not None:
            if not self.validate_monitored_status(value):
                raise ValueError('invalid value for monitored_status')
            self.update_favs('monitored_status', value)
            self.monitored_status = value

        value = data.get('slack_webhook')
        if value is not None:
            if value and not value.startswith('https://hooks.slack.com/services/'):
                raise ValueError('invalid value for slack_webhook')
            if not value:
                value = None
            self.update_favs('slack_webhook', value)
            self.slack_webhook = value

        self.save()

    @staticmethod
    def validate_monitored_status(l):
        if not isinstance(l, list):
            return False
        for key in l:
            if key not in Status.__members__:
                return False
        return True


    def as_dict(self):
        return {
            'username': self.username,
            'avatar_url': self.avatar_url,
            'monitored_status': self.monitored_status,
            'slack_webhook': self.slack_webhook,
        }
