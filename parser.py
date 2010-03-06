#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from ply import yacc
from lexer import Lexer
from lexer import TOKENS as tokens
from symboltable import SymbolTable
import symbol


# Start symbol
def p_S(p):
    ''' S : TreeDefinition
    '''

def p_Slist(p):
    ''' S : S TreeDefinition
    '''

def p_tree_is_terminal(p):
    ''' TreeDefinition : ID IS Terminal
    '''

def p_tree_is_subtree(p):
    ''' TreeDefinition : ID IS Terminal LP Arglist RP
    '''

def p_arglist_is_tree(p):
    ''' Arglist : Terminal
    '''

def p_arglist_is_list_arglist(p):
    ''' Arglist : Arglist COMMA Terminal
    '''

def p_terminal_is_ID(p):
    ''' Terminal : ID
    '''

def p_terminal_is_STR(p):
    ''' Terminal : STR
    '''
    p[0] = symbol.Terminal(p.text)
    print p[0]



if __name__ == '__main__':
    import sys

    parser = yacc.yacc()
    
    if len(sys.argv) < 2:
        parser.parse(sys.stdin.read())
    else:
        parser.parse(open(sys.argv[1], "rt").read())
    

