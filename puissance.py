#!/usr/bin/env python3

import sys 

try:
    arg = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    resultat= arg ** arg2
    print(resultat)
except:
    print("veuillez entrer un nombre")