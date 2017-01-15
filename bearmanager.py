#!/usr/bin/python

# SNAKES AHEAD!!!
# Created by ogator on 1/16/2017.
import sys


# Gather our code in a main() function
import cmd, sys

from modules.bearmodules import BearModules

class BearManager(cmd.Cmd):
    intro = "         _____        _\n" \
                       "       d8888888b.   d888b   ,db\n" \
                       "     d888888888888888888888888.*\n" \
                       "    888888 88888888888 88 8888888o\n" \
                       "   8888888 888888888 8888 8888`~~   - BEAR MANAGER - \n" \
                       "   8888888 888888888 88888\n" \
                       "   888888 8888888888 8888\n" \
                       "  ## 88888  88888 ##  8888\n" \
                       " #### 88888      ###   8888\n" \
                       "###,,, 888,,,    ##,,,  88,,,\n"
    prompt = 'bear>'
    file = None

    # ----- basic bear manager commands -----
    def do_load(self, arg):
        print("Loading...", arg)
        return True

    def do_bye(self, arg):
        print('Thank you for using BearManager')
        self.close()
        return True

if __name__ == '__main__':
    BearModules()
    BearManager().cmdloop()
