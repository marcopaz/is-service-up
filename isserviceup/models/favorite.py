import datetime
from mongoengine import Document, StringField, DateTimeField


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

