# https://www.hackerrank.com/contests/projecteuler/challenges/euler010

#!/bin/python3

import sys

primes = [2, 3]

def extendPrimes(n):
    candidate = primes[-1] + 2
    while primes[-1] < n:
        if isPrime(candidate):
            primes.append(candidate)
        candidate += 2


def isPrime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


def primeSumBelowN(n):
    if primes[-1] < n:
        extendPrimes(n)
    return sum(p for p in primes if p <= n)


t = int(input().strip())
for a0 in range(t):
    print(primeSumBelowN(int(input().strip())))
