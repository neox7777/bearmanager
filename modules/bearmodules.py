#!/usr/bin/python

# SNAKES AHEAD!!!
# Created by ogator on 1/16/2017.
import os
import inspect


# BearModules are implemented as class instances
# For each module there is a class implementing it
class BearModules:
    def __init__(self):
        lst = os.listdir('modules')
        lst.remove("bearmodules.py")
        self.mod_names = []
        self.mods = {}
        for d in lst:
            s = os.path.abspath("modules") + os.sep + d
            if os.path.isdir(s) and os.path.exists(s + os.sep + "__init__.py"):
                self.mod_names.append(d)
        # load the modules
        for m in self.mod_names:
            m_imported = __import__("modules." + m, fromlist=["*"])
            for name in dir(m_imported):
                obj = getattr(m_imported, name)
                if inspect.isclass(obj):
                    self.mods[m] = obj
                    break
