'''
Creez un programme qui affiche la racine carrée d'un entier positif.
'''
import sys

def racine_carree():
    try:
        arg = int(sys.argv[1])
        resultat = arg ** (1/2)

        print(int(resultat))
    except:
        print("Entrez un nombre entier positif.")

if __name__ == '__main__':
    racine_carree()
    
