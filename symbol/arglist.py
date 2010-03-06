#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from symbol import Symbol

class Arglist(Symbol):
    def __init__(self, arglistOrTerminal, terminal = None):
        super(self.__class__, self).__init__()

        self.list = []

        if terminal is None:
            self.list += [arglistOrTerminal]
        else:
            self.list = arglistOrTerminal.list + [terminal]

    def __len__(self):
        return len(self.list)

    def __getitem__(self, key):
        return self.list[key]

    def __str__(self):
        return self.__class__.__name__ + ': [' + ', '.join(str(x) for x in self.list) + ']'

