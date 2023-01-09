'''
Creez un programme qui permet de determiner si l'argument
donné est pair ou impair
'''
#!/usr/bin/python3
import sys

def pair_impair():
    try:
        arg = int(sys.argv[1])

        if arg % 2 == 0:
            print("pair")
        else:
            print("impair")
    except:
        print("tu ne me la mettras pas")

if __name__ == '__main__':
    pair_impair()
