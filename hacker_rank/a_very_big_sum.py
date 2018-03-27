#!/bin/python3

# Complete the function aVeryBigSum which takes arguments, an integer and a
# long integer array and returns a long integer denoting the sum of all array
# elements.
# https://www.hackerrank.com/challenges/a-very-big-sum/problem

def aVeryBigSum(n, ar):
    return sum(ar)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
