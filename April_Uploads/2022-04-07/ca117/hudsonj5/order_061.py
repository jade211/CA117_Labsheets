#!/usr/bin/env python3

import sys

def find(word):  # ("angelic", "novice", etc)
    result_words = []
    for word in word_list:  # "angelic"
        if word.count("n") == 1 and word.count("i") == 1 and word.count("c") == 1 and word.count("e") == 1:
            result_words.append(word)
    return result_words

def order(result):
    ordered = []
    for word in result:
        n = word.index("n")
        i = word.index("i")
        c = word.index("c")
        e = word.index("e")
        if (n < i and n < c and n < e) and (i > n and i < c and i < e) and (c > n and c > i and c < e) and (e > n and e > i and e > c):
            ordered.append(word)
    return ordered


word_list = []
for word in sys.stdin:
    word = word.strip()
    word_list.append(word)
result = find(word_list)
ordered = (order(result))
if len(ordered) > 0:
    print("\n".join(ordered))
