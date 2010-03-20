#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import unittest
from lexer import Lexer, MODE_EXCEPT
from gptreeserror import GPTreesError

class TestLexer(unittest.TestCase):
    ''' Test GPTrees scanner
    '''
    def setUp(self):
        self.lexer = Lexer(mode = MODE_EXCEPT) 

    def testError(self):
        ''' Test for invalid character
        '''
        self.lexer.input('$')
        self.assertRaises(GPTreesError, self.lexer.token)

    def testTokens(self):
        ''' Test for some tokens
        '''
        self.lexer.input("Ident ( ) 'string' , --> | ;")
        tokens = 'ID', 'LP', 'RP', 'STRING', 'COMMA', 'IS', 'OR', 'SC'
        for token in tokens:
            self.assertEqual(token, self.lexer.token().type)



