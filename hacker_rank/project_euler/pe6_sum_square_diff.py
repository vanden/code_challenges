# https://www.hackerrank.com/contests/projecteuler/challenges/euler006
 
#!/bin/python3

import sys

def squareSum(n):
    sSum = sum(range(1, n+1))
    return sSum * sSum

def sumSquares(n):
    return sum((x * x for x in range(1, n+1)))


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(abs(squareSum(n)) - sumSquares(n))
