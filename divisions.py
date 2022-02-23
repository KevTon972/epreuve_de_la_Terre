#!/usr/bin/env python3

import sys

try:
    arg = int(sys.argv[1])
    arg2 = int(sys.argv[2])
    resultat= (arg // arg2)
    reste =  (arg % arg2)
except:
    print("erreur.")
    quit()

if len(sys.argv) > 2:
    if arg > arg2:
        print(f"resultat: {resultat}")
        print(f"reste: {reste}")
  
    elif arg < arg2:
        print("erreur.")


