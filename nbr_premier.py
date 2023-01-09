'''
Creez un programme qui affiche si un nombre est premier ou pas.
'''
import sys

def nbr_premier():
    try:
        arg = int(sys.argv[1])

        if arg > 1:
            for i in range(2, arg):
                if (arg % i) == 0:
                    print(f"Non, {arg} n’est pas un nombre premier.")
                    return
            else:
                print(f"Oui, {arg} est un nombre premier.")
        else:
            print("le nombre doit être superieur à 1.")
    except:
        print("Erreur d'argument.")

if __name__ == '__main__':
    nbr_premier()
    
