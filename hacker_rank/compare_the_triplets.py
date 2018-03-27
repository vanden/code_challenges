#!/bin/python3

# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def solve(a0, a1, a2, b0, b1, b2):
    a = 0
    b = 0
    for (ap, bp) in [(a0, b0), (a1, b1), (a2, b2)]:
        if ap > bp:
            a += 1
        elif bp > ap:
            b += 1
            
    print("%s %s" %(a, b))
            
[a0, a1, a2] = [int(x) for x in input().strip().split(' ')]
[b0, b1, b2] = [int(x) for x in input().strip().split(' ')]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
