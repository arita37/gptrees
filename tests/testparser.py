#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import unittest
import parser
from gptreeserror import GPTreesError



class TestParser(unittest.TestCase):
    ''' Test GPTrees scanner
    '''
    def setUp(self):
        parser.MODE = parser.MODE_EXCEPT
        self.parser = parser.parser
        self.TEST = parser._TEST_

    def __parseTEST(self, f1, f2):
        ''' Load and parses file f1, and compares its
        output with file f2
        '''
        return self.TEST(open(f1, 'rt').read()) == open(f2, 'rt').read()


    def testSyntaxError(self):
        ''' Test for a generic syntax error is produced on error examples
        '''
        self.assertRaises(GPTreesError, self.parser.parse, open('tests/input/error.s').read())
        self.assertRaises(GPTreesError, self.parser.parse, open('tests/input/undef.s').read())
        self.assertRaises(GPTreesError, self.parser.parse, open('tests/input/duplicated.s').read())
        self.assertRaises(GPTreesError, self.parser.parse, open('tests/input/duplicated2.s').read())

    def testSample(self):
        ''' Test the example produces the expected output.
        '''
        self.assertTrue(self.__parseTEST('tests/input/example.s', 'tests/output/example.out'))





