#!/bin/python3

# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "NO"
    if (x1 < x2 and v1 < v2):
        return "NO"
    if (x1 - x2) % (v2 - v1) == 0:
        return "YES"
# First, thought to do the brute thing. But, obviously the mod way is better.
#    while x1 < x2:
#        x1 += v1
#        x2 += v2
#        if x1 == x2:
#            return "YES"
    return "NO"
