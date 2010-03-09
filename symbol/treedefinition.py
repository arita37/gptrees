#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:

from treedef import TreeDef

class TreeDefinition(TreeDef):
    def __init__(self, name, tree_def):
        TreeDef.__init__(self, tree_def.terminal, tree_def.arglist) # Creats self.terminal and self.arglist
        self.name = name # Tree symbol (left side of the rule)

