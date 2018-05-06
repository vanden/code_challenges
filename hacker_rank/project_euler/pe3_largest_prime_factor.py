# https://www.hackerrank.com/contests/projecteuler/challenges/euler003

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    bestFactor = 1
    while n % 2 == 0:
        bestFactor = 2
        n = n//2
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            bestFactor = factor
            n = n//factor
        if n == 1:
            break
        else:
            factor += 2
    print(max(n, bestFactor))
