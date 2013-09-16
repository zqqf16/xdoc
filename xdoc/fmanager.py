#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

class Fmanager(object):
    '''File Manager'''

    INDEX_FILE = 'index.json'

    def __init__(self, root_path):
        self.root_path = root_path
        self.index = os.path.join(self.root_path, self.INDEX_FILE)

        if not os.path.isfile(self.index):
            self.__init_index()

    def __init_index(self):
        with open(self.index, 'w') as f:
            json.dump({}, f)

    def get_all_info(self):
        '''Get all informations from index'''

        with open(self.index, 'r') as f:
            all_info = json.load(f)

        return all_info

    def get_info(self, path):
        '''Get the information of given file'''

        all_info = self.get_all_info()
        if all_info.has_key(path):
            return all_info[path]
        else:
            return {}

    def update_info(self, path, title, **kwargs):
        '''Update the information'''

        info = {'title': title}
        info.update(kwargs)

        all_info = self.get_all_info()
        all_info[path] = info

        with open(self.index, 'w') as f:
            json.dump(all_info, f)

    def get_content(self, path):
        abs_path = os.path.join(self.root_path, path)
        if not os.path.isfile(abs_path):
            return None

        with open(abs_path, 'r') as f:
            return f.read().decode('utf-8')

        return None

    def update_content(self, path, content):
        abs_path = os.path.join(self.root_path, path)
        with open(abs_path, 'w') as f:
            f.write(content)

