#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Content = {
        "title": "Content Title",
        "body": "Main body",
    }

    Author = {
        "name": "Author name",
        "password": "Author password",
        "salt": "Salt",
        "drafts": [
            {
                "title": "title",
                "content_id": "content id",
                "date": "created date"
            },
        ],
    }

    Doc = {
        "title": "title",
        "tags": ["tag1", "tag2"],
        "category": "category",
        "view_count": "view count",
        "histories": [
            {
                "author_id": "author id",
                "content_id": "content id",
                "date": "date",
            }, 
        ],
    }
'''

from mongoengine import *

def init(name='xdoc', host='127.0.0.1', port=27017):
    connect(name, host=host, port=port)

class Content(Document):
    title = StringField()
    body = StringField()

class Draft(EmbeddedDocument):
    title = StringField()
    content_id = ObjectIdField()
    date = DateTimeField()

class Author(Document):
    name = StringField(primary_key=True)
    password = StringField()
    salt = StringField()
    drafts = ListField(EmbeddedDocumentField(Draft))

class Version(EmbeddedDocument):
    author_id = ObjectIdField()
    content_id = ObjectIdField()
    date = DateTimeField()

class Doc(Document):
    title = StringField()
    tags = ListField(StringField)
    category = StringField()
    view_count = IntField()
    versions = ListField(EmbeddedDocumentField(Version))
