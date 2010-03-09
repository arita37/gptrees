#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:


class GPTreesError(Exception):
    ''' This will define a generic exception object
    to be raised on GPTrees errors
    '''
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return 'GPTreesError: ' + self.msg
    
