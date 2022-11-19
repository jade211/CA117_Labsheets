#!/usr/bin/env python3

import sys
def checker(password):
    count = 0
    if any(char.isdigit() for char in password):
        count = count + 1
    if any(char.isupper() for char in password):
        count = count + 1
    if any(char.islower() for char in password):
        count = count + 1
    if any(not char.isalnum() for char in password):
         count = count + 1
    return count


for password in sys.stdin:
    password = password.strip()
    print(checker(password))
