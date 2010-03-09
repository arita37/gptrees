#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from terminal import Terminal

class ID(Terminal):
    ''' An ID terminal symbol
    '''
    def __str__(self):
        return self.text

