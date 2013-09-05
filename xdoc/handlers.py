#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import tornado.web

from parser import Parser

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self, **kwargs):
        self.repo = self.application.repo
        self.root_path = self.application.root_path
        self.parser = Parser()

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

class RawHandler(BaseHandler):
    def get(self, path):
        content = self.get_content(path)
        title = os.path.basename(path)
        self.write({'title': title, 'content': content})

    def get_content(self, path):
        '''Get content from file in working tree'''
        abs_path = os.path.join(self.root_path, path)
        if not os.path.isfile(abs_path):
            raise tornado.web.HTTPError(404)
        try:
            with open(abs_path) as f:
                return f.read().decode('utf-8')
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
