#!/bin/python3
# https://www.hackerrank.com/challenges/most-commons/problem

import sys
import collections

charCount = collections.defaultdict(int)

def sortF(c):
    return (-charCount[c], c)

if __name__ == "__main__":
    s = input().strip()
    for c in s:
        charCount[c] += 1
    chars = sorted(set(s), key=sortF)
    for i in range(3):
        print(chars[i], charCount[chars[i]])
    
