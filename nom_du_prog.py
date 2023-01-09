#!/usr/bin/env python3
'''Creez un programme qui affiche son nom de fichier.'''
import os

def file_name():
    chemin = os.path.basename('/root/dir/sub/file.txt')
    print(chemin)

if __name__ == '__main__':
    file_name()
