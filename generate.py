#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import sys
import parser as Parser
from parser import parser
from gptreeserror import GPTreesError
from montecarlo import monte_carlo
from grammar import Grammar


def generate(input_str):
    ''' Parses an input string and returns another one
    containing the generated program skeleton.
    '''
    HEADER, L, ENDCODE = parser.parse(input_str)

    result = 'from skel import Grammar\n'

    if HEADER is not None:
        result += HEADER + '\n'

    result = result + """

def generate(self):
    
    """

    result = ''

    grammar = Grammar(Parser.START_SYMBOL)
    if L:
        for T in L:
            grammar.addRule(T)

    result += grammar.generate(Parser.START_SYMBOL)

    if ENDCODE is not None:
        result += ENDCODE + '\n'

    return result
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        input = sys.stdin.read()
    else:
        input = open(sys.argv[1], 'rt').read()

    print generate(input)
    

