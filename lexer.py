#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import ply.lex as lex
from gptreeserror import GPTreesError

TOKENS = ('ID', 
    'LP', # Left parenthesis
    'RP', # Right parenthesis
    'STRING', # A literal string, e.g. '+'
    'COMMA', #
    'IS', # Derivation ::= or -->
    'OR', # Disjunction |
    'INLINECODE',
    'SC',  # Semocolon ;
    'EXPR', # A simple expression
)

MODE_NORMAL = 0 # On error, prints an error msg (default)
MODE_EXCEPT = 1 # On error, raises a GPTreeError exception


class Lexer(object):
    ''' Lexer embedded in a class so several Lexer instances
    can be used in the same program.
    '''

    states = (
            ('codeblock', 'exclusive'),
            )

    def __init__(self, tokens = TOKENS, mode = MODE_NORMAL):
        ''' Constructor: tokens = t-uple with TOKENS list
        '''
        self.lex = None
        self.tokens = tokens
        self.mode = mode

    def t_skip(self, t):
        r'[ \t]+' # Matches one or more spaces and tabs
        pass      # and skips them


    def t_newline(self, t):
        r'\r?\n' # Skips newline, but increases lineno counter
        t.lexer.lineno += 1
        

    def t_INITIAL_codeblock_error(self, t):
        ''' Error handling rule. Called on lexical error.
        '''
        msg = "illegal character '%s'" % t.value[0]

        if self.mode == MODE_EXCEPT:
            raise GPTreesError(msg)

        print msg

    
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

    def t_INLINECODE(self, t):
        r'%{([^%]|%(?!}))*%}'
        t.value = t.value[2:-2]
        t.lexer.lineno += t.value.count('\n')
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

    def t_INITIAL_LBRACKET(self, t):
        r'\{'
        self.lb_count = 1
        self.codeblock = ''
        t.lexer.begin('codeblock')

    def t_codeblock_LBRACKET(self, t):
        r'\{'
        self.lb_count += 1
        self.codeblock += t.value

    def t_codeblock_newline(self, t):
        r'\r?\n'
        self.codeblock += t.value
        t.lexer.lineno += 1

    def t_codeblock_EXPR(self, t):
        r'\}'
        self.lb_count -= 1

        if not self.lb_count:
            t.value = self.codeblock
            t.lexer.begin('INITIAL')
            return t

        self.codeblock += t.value
            
    def t_codeblock_anychar(self, t):
        r'[^\r\n{}]+'
        self.codeblock += t.value
        

    # ---

    def input(self, str):
        ''' Reads str as input for lexical analysis.
        '''
        self.input_data = str
        self.lex = lex.lex(object = self) # Creates a lexer instance
        self.lex.input(self.input_data)  # Fills internal lexer with str chars.

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


