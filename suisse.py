'''Create a script who takes 3 numbers
and print the middle value.
'''
import sys

def find_middle_value(arg):
    sorted_list = []
    try:
        if len(arg) < 3 or len(arg) > 3:
            print("the list must contained 3 numbers.")
            return

        # put numbers in a list and sort the list
        sorted_list.extend(arg)
        sorted_list.sort()

        # if all values in the list are the same print an error 
        if all (i == sorted_list[0] for i in sorted_list):
            print("numbers should be differents!")
            return

        # print the middle value
        print(sorted_list[1])
    except:
        print("It should be numbers")

if __name__ == '__main__':
    arg = sys.argv[1:]
    find_middle_value(arg)
