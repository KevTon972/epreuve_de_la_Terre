'''
Creez un programme qui affiche le résultat d'une puissance.
'''
import sys

def puissance_d_un_nombre():
    try:
        arg = int(sys.argv[1])
        arg2 = int(sys.argv[2])
        resultat= arg ** arg2

        if len(sys.argv) > 3:
            print("seul deux nombres sont acceptés.")
            return

        print(resultat)
    except:
        print("veuillez entrer deux nombres")

if __name__ == '__main__':
    puissance_d_un_nombre()
    
