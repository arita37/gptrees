#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et

import symbol

class SymbolTable(object):
    ''' A simple symbol table for storing ID and and
    its attributes.
    '''
    def __init__(self):
        self.table = {}
