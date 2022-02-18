#!/usr/bin/env python3

import sys
import string

def a_partir_de():
    alpha= string.ascii_lowercase
    arg= sys.argv[1]

    for lettre in alpha:
        if arg == alpha[13]:
            print(alpha[13:])
        break
        
a_partir_de()