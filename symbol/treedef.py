#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class TreeDef(Symbol):
    ''' Right side of a Tree definition rule.
    This object stores such information.
    '''
    def __init__(self, terminal, arglist = None):
        Symbol.__init__(self)
        self.terminal = terminal # 1st symbol in the right side
        self.arglist = arglist # Optional arglist


