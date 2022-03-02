#!/usr/bin/env python3

from datetime import datetime
import sys

arg  = sys.argv[1]
h24 = datetime.strptime(arg, "%H:%M")

h12 = h24.strftime("%I:%M%p")
print(h12)
