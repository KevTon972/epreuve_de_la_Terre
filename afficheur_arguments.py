'''
Creez un programme qui affiche les arguments qu'il reçoit ligne par ligne
'''
#!/usr/bin/python3
import sys

def afficheur():
    for arg in sys.argv:
        print(arg)

if __name__ == '__main__':
    afficheur()
