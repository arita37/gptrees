#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import sys

from ply import yacc
from lexer import Lexer, MODE_NORMAL, MODE_EXCEPT
from lexer import TOKENS as tokens
from gptreeserror import GPTreesError
import symbol

# Default parsing mode
MODE = MODE_NORMAL

# Default STDERR
STDERR = sys.stderr

# FILENAME of the current source code.
# Empty string for STDIN
FILENAME = ''

# Simple symbol table. Keys are nonterminals
SYMBOL_TABLE = {}

# Simple generators table. Keys are terminals
GENERATORS = {}

# First grammar symbol
START_SYMBOL = None


def _RESET_(mode = MODE_NORMAL):
    ''' Initializes parser status
    '''
    global MODE, STDERR, START_SYMBOL
    global FILENAME, SYMBOL_TABLE, GENERATORS

    MODE = mode
    STDERR = sys.stderr
    FILENAME = ''
    SYMBOL_TABLE = {}
    GENERATORS = {}
    START_SYMBOL = None


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
    for terminal in GENERATORS.keys(): # Check for undefined terminal generators
        if GENERATORS[terminal] is None:
            if SYMBOL_TABLE.get(terminal, None) is None: # Is it a terminal?
                syntax_error("Undefined generator for '%s'" % terminal)
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
    global START_SYMBOL

    try:
        p[0] = make_tree(symbol.ID(p[1]), p[3])
    except GPTreesError as s:
        syntax_error(s.msg, lineno = p.lineno(1))

    if START_SYMBOL is None:
        START_SYMBOL = p[1]


def p_tree_is_definition(p):
    ''' TreeDefList : TreeDefAction
    '''
    p[0] = [p[1]] # Make a list with a single node


def p_tree_is_list_definition(p):
    ''' TreeDefList : TreeDefList OR TreeDefAction
    '''
    p[0] = p[1] + [p[3]] # Concatenate


def p_treedefaction_default(p):
    ''' TreeDefAction : TreeDef
    '''
    p[0] = p[1]


def p_treedefaction_treedef_action(p):
    ''' TreeDefAction : TreeDef EXPR
    '''
    p[1].generator = eval('lambda _ :' + p[2])
    if not p[1].arglist: # A --> B { EXPR } | There can be only one EXPR for B
        if GENERATORS.get(p[1].first.text, None) is not None:
            syntax_error('Duplicated generator for terminal [%s]' % p[1], lineno = p.lineno(2))
        GENERATORS[p[1].first.text] = p[2]
    p[0] = p[1]


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
    if p[1] not in GENERATORS.keys():
        GENERATORS[p[1]] = None # Mark this element as a terminal
    p[0] = symbol.ID(p[1])


def p_terminal_is_STR(p):
    ''' Terminal : STRING
    '''
    p[0] = symbol.STRING(p[1])


def p_error(p):
    # Error production
    tok = yacc.token()
    if tok is None:
        syntax_error('Unexpected end of file')
    else:
        syntax_error('Unexpected token "%s"' % tok.value, lineno = tok.lineno)


def syntax_error(msg, lineno = None):
    ''' A syntax error msg.
    '''
    if lineno is not None:
        msg = str(lineno) + ': ' + msg

    if FILENAME != '':
        msg = FILENAME + ':' + msg

    if MODE == MODE_EXCEPT:
        raise GPTreesError(msg)

    STDERR.write(msg + '\n')
    sys.exit(1)


parser = yacc.yacc()


def _TEST_(inputstr):
    ''' This function is used to TEST the parser
    (see relative tests). Basically, a string input
    is passed, and an output string is returned
    containing parsing information, or a GPTreesError
    exception raised.
    '''
    _RESET_(mode = MODE_EXCEPT)

    HEADER, L, ENDCODE = parser.parse(inputstr)
    result = ''

    if HEADER is not None:
        result += HEADER + '\n'

    if L:
        sorted = list(L)
        sorted.sort()
        for T in sorted:
            result += str(T) + '\n'

    if ENDCODE is not None:
        result += ENDCODE + '\n'

    return result


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 2:
        HEADER, L, ENDCODE = parser.parse(sys.stdin.read())
    else:
        HEADER, L, ENDCODE = parser.parse(open(sys.argv[1], "rt").read())

    if HEADER is not None:
        print '# --- HEADER        ---'
        print HEADER
        print '# --- END of HEADER ---\n'

    if L:
        print '# --- GRAMMAR       ---'
        for T in L:
            print T
        print '# --- GRAMMAR END   ---'

    if ENDCODE is not None:
        print '\n# --- BODY          ---'
        print ENDCODE
        print '# --- END OF BODY   ---'
    

