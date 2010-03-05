#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class Terminal(Symbol):
    ''' A terminal (STR or ID)
    '''
    def __init__(self, text):
        super(self.__class__, self).__init__(text = text)



