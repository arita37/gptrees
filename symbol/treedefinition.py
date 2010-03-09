#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol
from gptreeserror import GPTreesError

class TreeDefinition(Symbol):
    ''' This class provides a complete tree definition.
    Each symbol can have multiple definition.
      S -> A
         | B
         | C (S1, S2...)
         | D (S1, S2...)

    All symbols A, B, C, D (the 1st on each rule definition)
    must be different.
    '''
    def __init__(self, left, treedef_list):
        ''' Constructor. Requires Symbol S and a list [ ] of
        TreeDefs objects
        '''
        Symbol.__init__(self)
        self.left = left # Tree symbol (left side of the rule, S symbol)
        self.defs = {}
        self.add_alternatives(treedef_list)

    @property
    def alternatives(self):
        return self.defs.values()

    def add_alternatives(self, treedef_list):
        for definition in treedef_list:
            id = definition.first.text # Gets the ID yy_text
            if self.defs.get(id, None): # Already a rule with this prefix?
                raise GPTreesError('Ambiguous definition for %s with symbol %s' % (left, id))

            self.defs[id] = definition

    def __str__(self):
        result = ''
        sep = str(self.left) + ' --> '

        for treedef in self.alternatives:
            result += sep + str(treedef) + '\n'
            sep = '    | '
    
        return result

