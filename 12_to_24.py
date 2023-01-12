'''Créez un programme qui transforme une heure
affichée en format 12h en format 24h.
'''
import sys
from datetime import datetime

def hours(arg):
    h12 = datetime.strptime(arg, "%I:%M%p")
    h24 = h12.strftime("%H:%M")

    print(h24)

if __name__ == '__main__':
    arg = sys.argv[1]
    hours(arg)
    
