#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class TreeDefinition(Symbol):
    def __init__(self, terminal, arglist = None):
        super(self.__class__, self).__init__()
        self.terminal = terminal
        self.arglist = arglist


