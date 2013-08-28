#!/usr/bin/env python
# -*- coding: utf-8 -*-

import markdown
from datetime import datetime

def get_date(string):
    '''Convert string to datetime.
       Need to support more formats...
       ToDo
    '''
    try:
        date = datetime.strptime(string, '%Y-%m-%d')
    except:
        date = datetime.now()
    return date

# Metadata handlers
META_HANDLERS = {
    'tag':      lambda x: x if x else [],
    'title':    lambda x: x[0] if x else '',
    'auther':   lambda x: x[0] if x else '',
    'created':  lambda x: get_date(x[0]) if x else datetime.now(),
    'modified': lambda x: get_date(x[0]) if x else datetime.now(),
}

class Reader(object):
    '''Read Markdown, return HTML'''

    def __init__(self):
        self._md = markdown.Markdown(extensions=['fenced_code', 'codehilite', 'meta'], 
                                     extension_configs={
                                         'codehilite': [ ('guess_lang', False) ]
                                     })
 
    def _parse_metadata(self, meta):
        res = {}
        for name, handler in META_HANDLERS.items():
            value = handler(meta.get(name, None))
            res[name] = value

        return res

    def read(self, string):
        content = self._md.reset().convert(string.strip(' \n'))
        meta = self._parse_metadata(self._md.Meta)
        return content, meta

    def read_from_file(self, path):
        with open(path, 'r') as f:
            document = f.read().decode('utf-8') 
        return self.read(document)

if __name__ == '__main__':
    r = Reader()
    content, meta = r.read_from_file('../example.md')
    print(content)
    print(meta)
