#!/usr/bin/env python3

import sys

def find(word):  # ("angelic", "novice", etc)
    result_words = []
    for word in word_list:  # "angelic"
        if word.count("n") == 1 and word.count("i") == 1 and word.count("c") == 1 and word.count("e") == 1:
            result_words.append(word)
    return result_words


word_list = []
for word in sys.stdin:
    word = word.strip()
    word_list.append(word)
result = find(word_list)
if len(result) > 0:
    print("\n".join(result))
