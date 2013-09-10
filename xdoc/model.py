#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Doc = {
        "id": "document id",
        "title": "document title",
        "tags": ["tag1", "tag2"],
        "category": "ctg",
        "content": "document content",
    }

    Author = {
        "name": "author name",
        "passwd": "password",
        "salt": "salt",
        "drafts": [{"body": "doc id", "date", "2013-9-10"},
                   {"body": "doc id", "date", "2013-9-10"}],
    }

    Doc = {
        "view_count": 123,
        "history": [{"body": ObjectID, "author": ObjectID, "date": "2013-9-10"},
                    {"body": ObjectID, "author": ObjectID, "date": "2013-9-10"}],
    }

'''

import pymongo

def get_db(name='xdoc', host='localhost', port=27017):
    client = pymongo.MongoClient(host, port)
    return client[name]




