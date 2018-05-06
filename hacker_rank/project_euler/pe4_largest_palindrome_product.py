# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

#!/bin/python3

import sys

def palindromes_less_than_n(n):
    n = n - 1
    while n:
        s = str(n)
        if is_palindrome(s):
            yield n
        n -= 1

def is_palindrome(s):
    while s:
        if s[0] != s[-1]:
            return False
        s = s[1:-1]
    return True

def factors_into_two_threedigit_nums(n):
    if n > 999 * 999 or n < 100 * 100:
        return False
    for num in range(100, 1001, 100):
        if n > num * num:
            candidate = num

    # It is passing as is, but I feel like I should also be able to put an
    # upper bound on the search; various efforts failed.
    while candidate < 1000:
        if n % candidate == 0:
            if n / candidate > 99 and n / candidate < 1000:
                return True
        candidate += 1
    return False


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for p in palindromes_less_than_n(n):
        if factors_into_two_threedigit_nums(p):
            print(p)
            break
