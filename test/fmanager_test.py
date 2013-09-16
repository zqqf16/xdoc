#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
from os.path import join, dirname, abspath

sys.path.insert(0, join(dirname(dirname(abspath(__file__)))))
from xdoc.fmanager import *

class TestModels(unittest.TestCase):
    
    def setUp(self):
        Fmanager.INDEX_FILE = 'test.json'
        self.f = Fmanager('/home/zorro/xdoc')

    def test_update(self):
        self.f.update_info(path='test.md', title='Test', category='test')
        info = self.f.get_info('test.md')
        print info
        self.assertEqual(info['title'], 'Test')
        self.assertEqual(info['category'], 'test')

    def tearDown(self):
        os.remove(self.f.index)
 
if __name__ == '__main__':
    unittest.main()
