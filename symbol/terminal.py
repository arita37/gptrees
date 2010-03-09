#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class Terminal(Symbol):
    ''' A terminal (STR or ID)
    '''
    def __init__(self, text):
        Symbol.__init__(self, text = text)

    def __str__(self):
        return self.symbol_name

