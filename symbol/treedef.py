#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class TreeDef(Symbol):
    ''' This object stores the Right Side of a rule definition.
    '''
    def __init__(self, terminal, arglist = None, generator = None):
        Symbol.__init__(self)
        self.first = terminal # 1st symbol in the right side
        self.arglist = arglist # Optional arglist

        # If no generator specified, a default one is created
        # which will just return a string of the terminal
        if generator is None: 
            generator = lambda *args, **kwargs : self.first.text
        self.generator = generator # Optional generator function

    def __str__(self):
        ''' string representation of this object.
        '''
        result = str(self.first)
        if self.arglist:
            result += ' ' + str(self.arglist) 

        return result
        
    @property
    def is_terminal(self):
        return self.arglist is None

    @property
    def name(self):
        ''' If this tree definition is a terminal, it will
        returns the IDentifier name or the STRING yy_text. 
        Otherwise, it will return None
        '''
        return self.first.text if self.is_terminal else None
