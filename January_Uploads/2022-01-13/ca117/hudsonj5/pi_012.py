#!/usr/bin/env python3

import sys
from math import pi

for number in sys.stdin:
   n = int(number)
   print(f"{pi:.{n}f}")
