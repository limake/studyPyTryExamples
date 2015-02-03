#-------------------------------------------------------------------------------
# Name:        mydict_test
# Purpose:
#
# Author:      Administrator
#
# Created:     26/01/2015
# Copyright:   (c) Administrator 2015
# Licence:     <your licence>
#------------------------------------------------------------------------------

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        print 'setUp...'

    def tearDown(self):
        print 'tearDown...'

    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEquals(d.a,1)
        self.assertTrue(isintance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty







if __name__ == '__main__':
    unittest.main()
