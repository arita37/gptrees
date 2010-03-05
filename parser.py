#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from ply import yacc
from lexer import Lexer
from lexer import TOKENS as tokens


# Start symbol
def p_S(p):
    ''' S : treeDefinition
    '''

def p_Slist(p):
    ''' S : S treeDefinition
    '''

def p_tree_is_terminal(p):
    ''' treeDefinition : ID IS terminal
    '''

def p_tree_is_subtree(p):
    ''' treeDefinition : ID IS terminal LP arglist RP
    '''

def p_arglist_is_tree(p):
    ''' arglist : terminal
    '''

def p_arglist_is_list_arglist(p):
    ''' arglist : arglist COMMA terminal
    '''

def p_terminals(p):
    ''' terminal : ID
                 | STR
    '''
    


if __name__ == '__main__':
    import sys

    parser = yacc.yacc()
    parser.parse(sys.stdin.read(), debug = True)
    

