#!/usr/bin/env python3

import sys

def binsearch_reverse(fiveplus, reverse_words):
   low = 0
   high = len(fiveplus) - 1
   while low < high:
      mid = (low + high) // 2
      if fiveplus[mid].lower() < reverse_words:
         low = mid + 1
      else:
         high = mid
   return fiveplus[low].lower() == reverse_words


def main():
   list = []
   fiveplus = []
   for words in sys.stdin:
      words = words.strip()
      list.append(words)
      if len(words) >= 5:
         fiveplus.append(words)
   print([words for words in fiveplus if binsearch_reverse(fiveplus, words[::-1].lower())])


if __name__ == "__main__":
   main()
