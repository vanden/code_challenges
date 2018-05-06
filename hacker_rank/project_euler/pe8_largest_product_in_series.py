#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler008
#!/bin/python3


import sys
import functools

# A Naive solution first: (And, to my surprise, it is fast enough)

def substrings(string, length):
    start = 0
    while start + length < len(string) +1:
        yield string[start:start+length]
        start += 1


t = int(input().strip())
for a0 in range(t):
    n,k = [int(x) for x in input().strip().split(' ')]
    num = input().strip()
    best = 0
    for ss in substrings(num, k):
        best = max(best,
                   functools.reduce(lambda x, y: x * y,
                                    (int(x) for x in list(ss))))
    print(best)
