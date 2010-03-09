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
    defs = {}

    def __init__(self, name, treedef_list):
        ''' Constructor. Requires Symbol S and a list [ ] of
        TreeDefs objects
        '''
        Symbol.__init__(self)
        self.name = name # Tree symbol (left side of the rule)

        for definition in treedef_list:
            if self.defs.get(definition.first, None): # Already a rule with this prefix?
                raise GPTreesError('Ambiguous definition for %s with symbol %s' % (name, definition.first))

            self.defs[definition.first] = definition
            

    def __str__(self):
        result = ''
        sep = str(self.name) + ' --> '

        for treedef in self.defs.values():
            result += sep + str(treedef) + '\n'
            sep = '    | '
    
        return result

