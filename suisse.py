#!/usr/bin/env python3

import sys

arg = sys.argv[1:]
tri = []

#regrouper les arguments dans une liste triée
tri.extend(arg)
tri.sort()

#si toutes les valeurs de la liste sont identiques renvoyer "erreur." 
if all (i == tri[0] for i in tri):
    print("erreur.")
    exit()

#afficher la valeur du milieu
print(tri[1])
