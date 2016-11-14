import datetime
from mongoengine import StringField, Document, DateTimeField, BooleanField


class User(Document):
    username = StringField(required=True, unique=True)
    avatar_url = StringField()
    github_access_token = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    slack_webhook = StringField()

    def as_dict(self):
        return {
            'username': self.username,
            'avatar_url': self.avatar_url,
            'slack_webhook': self.slack_webhook,
        }
