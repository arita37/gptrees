#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import ply.lex as lex

TOKENS = ('ID', 
    'LP', # Left parenthesis
    'RP', # Right parenthesis
    'STR', # A literal string, e.g. '+'
    'COMMA', #
    'IS', # Derivation ::= or -->
)



class Lexer(object):
    ''' Lexer embedded in a class so several Lexer instances
    can be used in the same program.
    '''
    states = (
        ('string', 'exclusive'),
    )

    def __init__(self, tokens = TOKENS):
        ''' Constructor: tokens = t-uple with TOKENS list
        '''
        self.lex = None
        self.tokens = tokens

    def t_skip(self, t):
        r'[ \t\n]+' # Matches one or more spaces and tabs
        pass      # and skips them

    def t_string_INITIAL_error(self, t):
        ''' Error handling rule. Called on lexical error.
        '''
        print "illegal character '%s'" % t.value[0]

    # --- TOKENS patterns --- #

    def t_STR(self, t):
        r"'" # Start of string
        t.lexer.begin('string')
        self.__str = ''             # Initializes string buffer

    def t_string_ESCCHAR(self, t):
        r'\\.'
        self.__str += t.value[-1]   # Append matched text last char

    def t_string_CHRSTR(self, t):
        r"[^'\\]+"
        self.__str += t.value  # Append matched text *except* last char

    def t_string_STR(self, t):
        r"'"
        t.lexer.begin('INITIAL')    # Exits string stated. Back to INITIAL
        t.value = self.__str
        return t

    def t_LP(self, t):
        r'\('
        return t

    def t_RP(self, t):
        r'\)'
        return t

    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z\d]*'
        return t

    def t_COMMA(self, t):
        r','
        return t

    def t_IS(self, t):
        r'-->|::='
        return t

    # ---

    def input(self, str):
        ''' Reads str as input for lexical analysis.
        '''
        self.input_data = str
        self.lex = lex.lex(object = self) # Creates a lexer instance
        self.lex.input = self.input_data  # Fills internal lexer with str chars.

    def token(self):
        ''' Returns next token to the parser
        '''
        return self.lex.token()


# Creates a dummy instance needed to create lexer states
tmp = lex.lex(object = Lexer(), lextab = 'lextab')

if __name__ == '__main__':
    import sys
    
    tmp.input(sys.stdin.read())
    while True:
        token = tmp.token()
        if not token:
            break
        print token


