#!/usr/bin/env python3

import sys

def plural(word):
    if word.endswith("ch") or word.endswith("sh") or word.endswith("x") or word.endswith("s") or word.endswith("z"):
        return word + "es"
    if word.endswith("y") and word[-2:] != "ay" and word[-2:] != "ey" and word[-2:] != "iy" and word[-2:] != "oy" and word[-2:] != "uy":
        return word[:- 1] + "ies"
    if word.endswith("f"):
        return word[: - 1] + "ves"
    if word.endswith("fe"):
        return word[: - 2] + "ves"
    if word.endswith("o"):
        return word + "es"
    else:
        return word + "s"


for word in sys.stdin:
    word = word.strip()
    print(plural(word))
