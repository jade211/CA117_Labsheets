#!/usr/bin/env python3

def power(m, n):
   if n == 0:  # base case
      return 1
   return m * power(m, n - 1)

# step 1 - power(2, 3), will return 2 * (2, 3 - 1 (gives 2))
# step 2 - power(2, 2,) will return 2 * (2, 2 - 1 (gives 1))
# step 3 - power(2, 1) will return 2 * (2, 1 - 1 (gives 0))
# step 4 - power(2, 0) will return 2 * (1) because n == 0
# step 5 - multiplies return values by m each time, (1*2, 2*2, 4*2, 4*2 = 8)
