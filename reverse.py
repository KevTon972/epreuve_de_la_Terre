'''
Creez un programme qui affiche l'inverse de la
chaine de caractères donnée.
'''
import sys

def reverse_string():
    try:
        chaine = sys.argv[1]

        if chaine.isdigit():
            print("L'argument doit être une chaîne de caractères.")
            return

        print(chaine[::-1])
    except:
        print("probleme d'argument.")

if __name__ == '__main__':
    reverse_string()
    
