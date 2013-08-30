#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import git

import config
import reader

class BaseObject(object):
    root_path = config.ROOT_PATH

    def __init__(self, path):
        self.path = path
        self.reader = reader.Reader()
        self.abspath = os.path.join(self.root_path, path)
        self.content = None
        self._meta = None
        self._body = None
        self.initialize()

    def initialize(self):
        pass

    def parse(self):
        self._body, self._meta = self.reader.read(self.content)

    @property
    def body(self):
        if self._body:
            return self._body
        self.parse()
        return self._body

    @property
    def meta(self):
        if self._meta:
            return self._meta
        self.parse()
        return self._meta

class Draft(BaseObject):

    def initialize(self):
        with open(self.abspath, 'r') as f:
            self.content = f.read().decode('utf-8')

    def discard(self):
        pass

    def save(self):
        pass

class Document(BaseObject):
    repo = git.Repo(config.ROOT_PATH)
    
    def initialize(self):
        self.blob = self.repo.head.commit.tree[self.path]
        self.content = self.blob.data_stream.read()

if __name__ == '__main__':
    example = Draft('example.md')
    print example.meta
    doc = Document('example.md')
    print doc.meta
