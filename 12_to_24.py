#!/usr/bin/env python3

import sys
from datetime import datetime

arg = sys.argv[1]

h12 = datetime.strptime(arg, "%I:%M%p")

h24 = h12.strftime("%H:%M")

print(h24)