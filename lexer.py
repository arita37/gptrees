#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import ply.lex as lex

TOKENS = ('ID', 
    'LP', # Left parenthesis
    'RP', # Right parenthesis
    'STRING', # A literal string, e.g. '+'
    'COMMA', #
    'IS', # Derivation ::= or -->
    'OR', # Disjunction |
    'HEADERSECTION',
    'SC'  # Semocolon ;
)



class Lexer(object):
    ''' Lexer embedded in a class so several Lexer instances
    can be used in the same program.
    '''
    def __init__(self, tokens = TOKENS):
        ''' Constructor: tokens = t-uple with TOKENS list
        '''
        self.lex = None
        self.tokens = tokens

    def t_skip(self, t):
        r'[ \t]+' # Matches one or more spaces and tabs
        pass      # and skips them


    def t_newline(self, t):
        r'\r?\n' # Skips newline, but increases lineno counter
        t.lexer.lineno += 1
        

    def t_error(self, t):
        ''' Error handling rule. Called on lexical error.
        '''
        print "illegal character '%s'" % t.value[0]

    
    def t_linecomment(self, t):
        r'\#.*'
        # --- Skip from # to EOL

    # --- TOKEN patterns --- #

    def t_STRING(self, t):
        r"'([^'\\]|\\.)*'"
        t.value = t.value[1:-1] # remove single quotes
        return t

    def t_LP(self, t):
        r'\('
        return t

    def t_RP(self, t):
        r'\)'
        return t

    def t_HEADERSECTION(self, t):
        r'%{([^%]|%(?!}))*%}'
        t.value = t.value[2:-3]
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

    def t_OR(self, t):
        r'\|'
        return t

    def t_SC(self, t):
        r';'
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


