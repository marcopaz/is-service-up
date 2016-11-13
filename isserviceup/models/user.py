import datetime
from mongoengine import StringField, Document, DateTimeField


class User(Document):
    username = StringField(required=True, unique=True)
    avatar_url = StringField()
    github_access_token = StringField()
    timestamp = DateTimeField(default=datetime.datetime.now)
