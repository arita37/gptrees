#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

class Symbol(object):
    ''' A grammar symbol.
    '''
    isTerminal = None
    text = None # If isTerminal => the recognized text
    token = None # The symbol name as a string

    def __init__(self, token = None, text = None):
        if token is None:
            token = self.__class__.__name__
    
        self.token = token
        self.text = text
        self.isTerminal = text is not None
    

