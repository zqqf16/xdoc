#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    Draft = {
        "title"
        "content"
    }

    Author = {
        "name"
        "password"
        "salt"
        "drafts" [{"title" "draft" "date"}]
    }

    Document = {
        "title"
        "category"
        "view_count"
        "histories": [ {"author" "draft" "date"}, {"author" "draft" "date"}],
    }
'''

import pymongo

def get_db(name='xdoc', host='localhost', port=27017):
    client = pymongo.MongoClient(host, port)
    return client[name]




