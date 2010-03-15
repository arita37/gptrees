#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import sys
from parser import parser


def generate(input_str):
    ''' Parses an input string and returns another one
    containing the generated program skeleton.
    '''
    HEADER, L, ENDCODE = parser.parse(input_str)

    result = ''

    if HEADER is not None:
        result += HEADER + '\n'

    result = result + """
class Generator(object):
    def generate(self):
        
    


    if ENDCODE is not None:
        result += ENDCODE + '\n'

    return result
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        input = sys.stdin.read()
    else:
        input = open(sys.argv[1], 'rt').read()

    print generate(input)
    

