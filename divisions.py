'''
Creez un programme qui affiche le résultat et le reste
d'une division entre 2 nombres
'''
#!/usr/bin/python3
import sys

def division():
    try:
        arg = int(sys.argv[1])
        arg2 = int(sys.argv[2])
        resultat= arg // arg2
        reste =  arg % arg2

        if arg2 > arg:
            print("erreur.")
            return

        print(f"resultat: {resultat}")
        print(f"reste: {reste}")
    except:
        print("erreur.")

if __name__ == '__main__':
    division()
