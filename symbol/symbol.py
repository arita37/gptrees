#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

class Symbol(object):
    ''' A grammar symbol.
    '''
    isTerminal = None
    text = None # If isTerminal => the recognized text
    symbol_name = None # The symbol name as a string

    def __init__(self, symbol_name = None, text = None):
        if symbol_name is None:
            symbol_name = self.__class__.__name__
    
        self.symbol_name = symbol_name 
        self.text = text
        self.isTerminal = text is not None
    
    def __str__(self):
        return self.symbol_name

