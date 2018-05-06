# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

#!/bin/python3

import sys
import functools

primes = [2,3]

def extendPrimes(n):
    candidate = primes[-1] + 2
    while primes[-1] <= n:
        if isPrime(candidate):
            primes.append(candidate)
        if candidate > n:
            break
        candidate += 2

def isPrime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True

def prime_factorization(n):
    extendPrimes(n)
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n = n // p
    return factors

def smallest_sequentially_divisible(n):
    if n == 1:
        return 1
    factors = []
    for factor in range(2, n+1):
        newFactors = prime_factorization(factor)
        updatedFactors = []
        for f in set(factors).union(set(newFactors)):
            fCount = max(newFactors.count(f), factors.count(f))
            updatedFactors.extend([f] * fCount)
        factors = updatedFactors

    return functools.reduce(lambda x, y: x*y, factors)


t = int(input().strip())
for a0 in range(t):
     n = int(input().strip())
     print(smallest_sequentially_divisible(n))
