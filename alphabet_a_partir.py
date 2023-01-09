'''
Creez un programme qui affiche l'alphabet
à partir de la lettre donner en argument en minuscule
'''
#!/usr/bin/python3
import sys
import string

def a_partir_de():
    alpha= string.ascii_lowercase
    arg= sys.argv[1]

    if arg in alpha:
        idx = alpha.index(arg)
        print(alpha[idx:])

if __name__ == '__main__':
    a_partir_de()
