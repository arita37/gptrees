#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from terminal import Terminal

class ID(Terminal):
    ''' An ID terminal symbol
    '''
    def __init__(self, text, generatorFunc = None):
        Terminal.__init__(self, text)

        if generatorFunc is None:
            generatorFunc = lambda _: text

        self.generator = generatorFunc

    def __str__(self):
        return self.text

    def __call__(self):
        return self.generator()

