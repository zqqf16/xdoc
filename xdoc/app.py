#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import tornado.ioloop
import tornado.httpserver
import tornado.web
from tornado.options import define, options
import git

from handlers import *

define("port", default=8888, help="run on the given port", type=int)
define("path", default='./', help="run on the given path", type=str)

class XdocApp(tornado.web.Application):
    def __init__(self, root_path):
        self.repo = git.Repo(root_path)
        self.root_path = root_path

        handlers = [
            (r'/view/(.*)', ViewHandler),
            (r'/raw/(.*)', RawHandler),
            (r'[/]?', ListHandler),
        ]

        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "static_path": os.path.join(os.path.dirname(__file__), "static"),
            "login_url": "/login",
        }

        super(XdocApp,self).__init__(handlers, **settings)

if __name__ == '__main__':
    options.parse_command_line()
    XdocApp(options.path).listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
