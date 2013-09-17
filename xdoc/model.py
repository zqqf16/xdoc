#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongoengine import *
from bson.objectid import ObjectId
from datetime import datetime
import json

def db_init(name='xdoc', host='127.0.0.1', port=27017):
    connect(name, host=host, port=port)

class Author(Document):
    name = StringField(unique=True)
    password = StringField()
    salt = StringField()
    email = EmailField()

class Doc(Document):
    uuid = StringField()
    status = StringField(default="draft")
    title = StringField()
    tags = ListField(StringField)
    category = StringField()
    created = DateTimeField(default=datetime.now())
    modified = DateTimeField(default=datetime.now())
    view_count = IntField(default=0)
    author = ReferenceField(Author)
    content = StringField()

    def fork(self):
        return Doc(uuid=self.uuid, title=self.title, tags=self.tags,
                   category=self.category, created=self.created,
                   view_count=self.view_count, content=self.content)

    def json(self):
        fields = {
            'uuid': self.uuid,
            'status': self.status,
            'title': self.title,
            'tags': self.tags,
            'category': self.category,
            'created': self.created.strftime('%Y-%m-%d'),
            'modified': self.modified.strftime('%Y-%m-%d'),
            'view_count': self.view_count,
            'content': self.content,
        }

        return json.dumps(fields)
