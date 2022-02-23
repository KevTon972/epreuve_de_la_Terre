#!/usr/bin/env python3

import sys

try:
    arg = int(sys.argv[1])
    resultat = arg ** (1/2)

    print(int(resultat))
except:
    print("entrez un nombre")