#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import json
import tornado.web

from parser import Parser
from utils import *
from fmanager import Fmanager

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.repo = self.application.repo
        self.root_path = self.application.root_path
        self.parser = Parser()
        self.f = Fmanager(self.root_path)

    def get_error_html(self, code, **kwargs):
        self.write(str(code))

class ViewHandler(BaseHandler):
    def get(self, path):
        md = self.get_content(path)
        content, meta = self.parser.parse(md)
        self.render('view.html', title=meta.get('title'), content=content)

    def get_content(self, path):
        '''Get content from blob'''
        try:
            blob = self.repo.head.commit.tree[path]
        except:
            raise tornado.web.HTTPError(404)
        try:
            return blob.data_stream.read().decode('utf-8')
        except:
            raise tornado.web.HTTPError(500) 

class EditHandler(BaseHandler):
    def get(self, path):
        self.render('edit.html')

class ListHandler(BaseHandler):
    def get(self):
        tree = self.repo.head.commit.tree
        blobs = [item for item in tree.traverse() if item.type=='blob']
        self.render('list.html', title="All", docs=blobs)

#REST
class CategoryHandler(BaseHandler):
    def get(self):
        trees = [t.path for t in self.repo.head.commit.tree.trees]
        self.write({"categories": trees})

class DraftHandler(BaseHandler):
    def get(self):
        path = self.get_argument('path', '')

        content = self.f.get_content(path)
        if not content:
            raise tornado.web.HTTPError(404)
            
        info = self.f.get_info(path)
        title = info['title']
        self.write({'title': title, 'content': content, 'path': path})

    def post(self):
        arguments = json.loads(self.request.body)
        title = arguments['title']
        content = arguments['content']
        path = arguments['path']
        self.f.update_info(path=path, title=title)
        self.f.update_content(path=path, content=content)
