#!/usr/bin/env python3

import sys
list = []

for word in sys.stdin:
   word = word.strip()
   list.append(word)

print(f"Words containing 17 letters: {[word for word in list if len(word) == 17]}")
print(f"Words containing 18+ letters: {[word for word in list if len(word) >= 18]}")
print(f"Words with 4 a's: {[word for word in list if word.lower().count('a') == 4]}")
print(f"Words with 2+ q's: {[word for word in list if word.lower().count('q') >= 2]}")
print(f"Words containing cie: {[word for word in list if 'cie' in word.lower()]}")
print(f"Anagrams of angle: {[word for word in list if 'a' in word.lower() and 'n' in word.lower() and 'g' in word.lower() and 'l' in word.lower() and 'e' in word.lower() and len(word) == 5 and word.lower() != 'angle']}")
