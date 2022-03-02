#!/usr/bin/env python3
 
import sys

arg = sys.argv[1:]
liste = []

#regrouper les arguments dans une liste triée
liste.extend(arg)

#parcourir la liste et verifier si les valeurs sont triées ou non
for i in liste:

    if i > liste[0]:
        print("triée!")
        exit()

    elif i < liste[0]:
       print("pas triée!")
       exit()
else:
   print("erreur.")