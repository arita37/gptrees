#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class TreeDefinition(Symbol):
    def __init__(self, name, terminal, arglist = None):
        Symbol.__init__(self)
        self.name = name # Tree symbol (left side of the rule)
        self.terminal = terminal # 1st symbol in the right side
        self.arglist = arglist # Optional arglist


