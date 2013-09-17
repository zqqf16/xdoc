#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import json
import tornado.web

from parser import Parser
from model import *
from bson.objectid import ObjectId

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.parser = Parser()
        print 'ahah'
        db_init()

    def get_error_html(self, code, **kwargs):
        self.write(str(code))

#REST
class DraftHandler(BaseHandler):
    def get(self, obj_id = None):
        try:
            if not object_id:
                draft = [d.json for d in Doc.objects]
            else:
                draft = Doc.objects.get(id=ObjectId(obj_id))
        except:
            raise tornado.web.HTTPError(404)

        if not draft:
            raise tornado.web.HTTPError(404)

        self.write(draft.json())

    def put(self):
        pass

    def post(self):
        arguments = json.loads(self.request.body)
        path = arguments['path']

    def delete(self):
        pass
