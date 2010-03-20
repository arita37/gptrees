#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

import sys
import parser as Parser
from parser import parser
from gptreeserror import GPTreesError
from montecarlo import monte_carlo



class Rule(object):
    ''' Describes a rule.
    '''
    def __init__(self, grammar, left, right):
        self.left = left
        self.right = right
        self.generator = right.generator
        self.grammar = grammar # Grammar object containing this rule

    def __str__(self):
        return str(self.left) + ' --> ' + str(self.right)

    def generate(self, *args):
        ''' Calling this rule invokes its generator
        If called with no arguments, it will return
        the result of the 1st generator
        '''
        if self.right.is_terminal:   # Not a subtree
            return self.right.generator()

        _ = []
        for i in self.right.arglist:
            _ += [self.grammar.generate(i.text)]

        if self.generator is None:
            return _[0]

        return self.generator(_)

    def __call__(self, *args):
        self.generate(*args)
        


class Grammar(object):
    ''' Describes grammar rules
    '''
    def __init__(self, startSymbol):
        self.symbols = {} # Symbols
        self.probs = {} # Probabilities
        self.start = startSymbol

    def addRule(self, treeDefinition):
        symbol = treeDefinition.left.text
        self.symbols[symbol] = [] # Initializes with an empty array
        self.probs[symbol] = [] # Probabilities for each alternative

        for right in treeDefinition.alternatives:
            self.symbols[symbol] += [Rule(self, symbol, right)] # Add the rule to the list 
            self.probs[symbol] += [1.0]

        LS = self.probs[symbol]
        self.probs[symbol] = [x / len(LS) for x in LS] # Probability

    def generate(self, S = None, *args):
        ''' Generates the output for a symbol S
        '''
        if S is None:
            S = self.start

        return monte_carlo(self.symbols[S], self.probs[S]).generate(*args)

    def __call__(self, symbol, *args):
        return self.generate(symbol, *args)
        


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
    """

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
    

