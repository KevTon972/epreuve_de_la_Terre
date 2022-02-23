#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("erreur.")
    exit()

elif len(sys.argv) >2:
    print("erreur.")
    exit()
    
try:
    chaine = int(sys.argv[1])
    print("erreur.")
except:
    print(len(sys.argv[1]))