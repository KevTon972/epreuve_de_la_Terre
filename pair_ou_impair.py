#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
    print("tu ne me la mettras pas")
    exit()

try:
    arg = int(sys.argv[1])
    if arg % 2 ==0:
        print("pair")
    else:
        print("impair")
except:
    print("tu ne me la mettras pas")
