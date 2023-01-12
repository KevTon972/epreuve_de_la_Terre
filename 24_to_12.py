'''Créez un programme qui transforme une heure
affichée en format 24h en format 12h.
'''
from datetime import datetime
import sys

def hours(arg):
    h24 = datetime.strptime(arg, "%H:%M")
    h12 = h24.strftime("%I:%M%p")

    print(h12)

if __name__ == '__main__':
    arg  = sys.argv[1]
    hours(arg)
