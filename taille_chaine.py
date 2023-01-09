'''
Creez un programme qui affiche le nombre de caractères
d'une chaine de carctères donnée en argument.
'''
import sys

def lenght_string():
    try:
        string = sys.argv[1]

        if string.isdigit():
            print("l'argument doit etre une chaine de caractères.")
            return

        elif len(sys.argv) >2:
            print("Une seule chaine de caractères est autorisée.")
            return

        print(len(string))
    except:
        print("Veuillez donner un argument.")

if __name__ == '__main__':
    lenght_string()
    
