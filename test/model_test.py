#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest
from os.path import join, dirname, abspath
from bson.objectid import ObjectId

sys.path.insert(0, join(dirname(dirname(abspath(__file__)))))
from xdoc.model import *

class TestModels(unittest.TestCase):
    
    def setUp(self):
        init('test')

    def test_content(self):
        content = Content(title='content test', body='unit test')
        content.save()
        self.assertIsInstance(content.id, ObjectId)
        nc = Content.objects(id=content.id).first()
        self.assertEqual(nc.title, content.title)
        self.assertEqual(nc.body, content.body)


if __name__ == '__main__':
    unittest.main()
