#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import tornado.web

from reader import Reader

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.repo = self.application.repo
        self.root_path = self.application.root_path

class ViewHandler(BaseHandler):
    def get(self, path):
       blob = self.repo.head.commit.tree[path]
       content = blob.data_stream.read()
       reader = Reader()
       body,meta = reader.read(content)
       self.write(body)

class RawHandler(BaseHandler):
    def get(self, path):
        blob = self.repo.head.commit.tree[path]
        content = blog.data_stream.read()
        self.write(content)

class EditHandler(BaseHandler):
    def get(self, path):
       abspath = os.path.join(self.root_path, path) 
       reader = Reader()
       body, meta = reader.read_from_file(abspath)
       self.write(body)

