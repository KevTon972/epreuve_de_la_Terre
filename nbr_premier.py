#!/usr/bin/env python3

import sys

arg = int(sys.argv[1])

if arg > 1:
    
    for i in range(2, arg):
 
              
        if (arg % i) == 0:
            print(f"Non, {arg} n’est pas un nombre premier.")
            break
    else:
        print(f"Oui, {arg} est un nombre premier.")
 
else:
    print(f"Non, {arg} n’est pas un nombre premier.")