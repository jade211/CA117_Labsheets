#!/usr/bin/env python3

import sys

def qnou(word):
   word = word.lower()
   word = word.replace("qu", "")
   if "q" in word:
      return True


qnous = [word.strip() for word in sys.stdin if qnou(word)]

print(f"Words with q but no u: {qnous}")
