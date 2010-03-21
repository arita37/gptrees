#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import re
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
        self.reERR_AMBI = re.compile('[0-9]+: Duplicated generator for terminal \[[^\]]+]')

    def __parseTEST(self, f1, f2):
        ''' Load and parses file f1, and compares its
        output with file f2
        '''
        tmp = self.TEST(open(f1, 'rt').read()).split('\n')
        a = [x.rstrip() for x in tmp if x.rstrip() != '']
        b = [x.rstrip() for x in open(f2, 'rt').read().split('\n') if x.rstrip() != '']
        
        return a == b


    def __ambiguousTEST(self, f1):
        try:
            self.TEST(open(f1).read())
        except GPTreesError, v:
            pass
        except:
            self.fail("ambiguous grammar undetected in file '%s'" % f1) 

        return self.reERR_AMBI.match('29: Duplicated generator for terminal [NUM]') is not None

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

    def testDuplicated(self):
        '''Test for ambiguous / duplicated definitions, case 1
        '''
        self.assertTrue(self.__ambiguousTEST('tests/input/duplicated.s'))

    def testDuplicated2(self):
        '''Test for ambiguous / duplicated definitions, case 1
        '''
        self.assertTrue(self.__ambiguousTEST('tests/input/duplicated2.s'))





