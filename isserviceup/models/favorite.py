import datetime
from mongoengine import Document, StringField, DateTimeField, ValidationError, ListField, URLField


class Favorite(Document):
    meta = {
        'indexes': [
            {'fields': ('user_id',) },
            {'fields': ('service_id',) },
            {'fields': ('user_id', 'service_id'), 'unique': True}
        ]
    }

    user_id = StringField(required=True)
    service_id = StringField(required=True)
    timestamp = DateTimeField(default=datetime.datetime.now)

    monitored_status = ListField(default=None)
    slack_webhook = URLField(default=None)

