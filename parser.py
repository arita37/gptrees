#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from ply import yacc
from lexer import Lexer
from lexer import TOKENS as tokens
import symbol


SYMBOL_TABLE = {}



def make_tree(id, treedef_list):
    ''' Returns a tree for the new ID.
    If the ID already exists, returns
    the existing tree, adding the treedef_list 
    to the rule alternatives.
    If for the given tree two rules start with the same
    prefix, an error is raised.
    '''
    result = SYMBOL_TABLE.get(id.text, None)
    if result: # There are alternatives for the given ID. So add the new ones
        result.add_alternatives(treedef_list)
    else: # There's no alternatives for the given ID. Create tree definition
        result = symbol.TreeDefinition(id, treedef_list)

    SYMBOL_TABLE[id.text] = result

    return result


'''
--------------------------
    Grammar Definition
--------------------------
'''
# Start symbol
def p_S(p):
    ''' S : optionalsection TreeList optionalsection
    '''
    p[0] = [p[1], p[2], p[3]]

def p_optional_section(p):
    ''' optionalsection : 
    '''
    p[0] = None # Epsilon

def p_optional_section_definition(p):
    ''' optionalsection : INLINECODE
    '''
    p[0] = p[1]

def p_treelist_treedefinition(p):
    ''' TreeList : TreeDefinition
    '''
    p[0] = set([p[1]])

def p_treelist_treelist_treedefinition(p):
    ''' TreeList : TreeList TreeDefinition
    '''
    p[1].add(p[2]) # Add the tree to de Set
    p[0] = p[1]

def p_tree_is_treedef_list(p):
    ''' TreeDefinition : ID IS TreeDefList SC
    '''
    p[0] = make_tree(symbol.ID(p[1]), p[3])

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

def p_arglist_is_tree(p):
    ''' Arglist : Terminal
    '''
    p[0] = symbol.Arglist(p[1])

def p_arglist_is_list_arglist(p):
    ''' Arglist : Arglist COMMA Terminal
    '''
    p[0] = symbol.Arglist(p[1], p[3])

def p_terminal_is_ID(p):
    ''' Terminal : ID
    '''
    p[0] = symbol.ID(p[1])

def p_terminal_is_STR(p):
    ''' Terminal : STRING
    '''
    p[0] = symbol.STRING(p[1])



if __name__ == '__main__':
    import sys

    parser = yacc.yacc()
    
    if len(sys.argv) < 2:
        HEADER, L, ENDCODE = parser.parse(sys.stdin.read())
    else:
        HEADER, L, ENDCODE = parser.parse(open(sys.argv[1], "rt").read())

    if HEADER is not None:
        print HEADER

    for T in L:
        print T

    if ENDCODE is not None:
        print ENDCODE
    

