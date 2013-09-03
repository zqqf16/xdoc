#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.web

from reader import Reader

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.repo = self.application.repo

class ViewHandler(BaseHandler):
    def get(self, path):
       blob = self.repo.head.commit.tree[path]
       content = blob.data_stream.read()
       reader = Reader()
       body,meta = reader.read(content)
       self.write(body)

