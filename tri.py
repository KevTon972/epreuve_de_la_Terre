#!/usr/bin/env python3
 
import sys

arg = sys.argv[1:]
liste = []

#regrouper les arguments dans une liste 
liste.extend(arg)

# verifier si les valeurs sont ordonnées ou non
try:
    if liste[0] > liste[1]:
        print("pas tiée!")
    elif liste[0] < liste[1]:
        if liste[1] < liste[2]:
            if liste[2] < liste[3]:
             print("triée!")
except: 
    print("erreur.")