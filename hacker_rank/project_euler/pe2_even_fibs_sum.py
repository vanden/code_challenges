#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

import sys

fibs = [1, 2]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while fibs[-1] < n:
        fibs.append(fibs[-1] + fibs[-2])
    print(sum(f for f in fibs if f%2 == 0 and f < n))
