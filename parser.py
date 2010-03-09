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
    p[0] = [p[1]]
    print p[0]

def p_Slist(p):
    ''' S : S TreeDefinition
    '''
    p[0] = p[1] + [p[2]]
    print p[0]

def p_tree_is_treedef_list(p):
    ''' TreeDefinition : ID IS TreeDefList
    '''
    p[0] = [symbol.TreeDefinition(symbol.ID(p[1]), T) for T in p[3]]
    print p[0]

def p_tree_is_definition(p):
    ''' TreeDefList : TreeDef
    '''
    p[0] = [p[1]] # Make a list with a single node

def p_tree_is_list_definition(p):
    ''' TreeDefList : TreeDefList OR TreeDef
    '''
    p[0] = p[1] + [p[3]] # Concatenate

def p_tree_is_terminal(p):
    ''' TreeDef : Terminal
    '''
    p[0] = symbol.TreeDef(p[1])

def p_tree_is_subtree(p):
    ''' TreeDef : Terminal LP Arglist RP
    '''
    p[0] = symbol.TreeDef(p[1], p[3])
    print p[0]

def p_arglist_is_tree(p):
    ''' Arglist : Terminal
    '''
    p[0] = symbol.Arglist(p[1])
    print p[0]

def p_arglist_is_list_arglist(p):
    ''' Arglist : Arglist COMMA Terminal
    '''
    p[0] = symbol.Arglist(p[1], p[3])
    print p[0]

def p_terminal_is_ID(p):
    ''' Terminal : ID
    '''
    p[0] = symbol.ID(p[1])
    print p[0]

def p_terminal_is_STR(p):
    ''' Terminal : STRING
    '''
    p[0] = symbol.STRING(p[1])
    print p[0]



if __name__ == '__main__':
    import sys

    parser = yacc.yacc()
    
    if len(sys.argv) < 2:
        parser.parse(sys.stdin.read())
    else:
        parser.parse(open(sys.argv[1], "rt").read())
    

