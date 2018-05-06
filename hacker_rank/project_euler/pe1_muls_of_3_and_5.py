#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n - 1
    threeSum = 3 * (n//3 * (n//3 + 1)) // 2 
    fiveSum = 5 * (n//5 * (n//5 + 1)) // 2 
    fifteenSum = 15 * (n//15 * (n//15 + 1)) // 2 
#    print(threeSum, fiveSum, fifteenSum)
    print(threeSum + fiveSum - fifteenSum)
