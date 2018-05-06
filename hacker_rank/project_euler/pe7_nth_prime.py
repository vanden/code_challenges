# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

#!/bin/python3

import sys

primes = [2,3,5,7]

def nthPrime(n):
    candidate = primes[-1]
    while len(primes) < n:
        candidate += 2
        if isPrime(candidate):
            primes.append(candidate)
    return primes[n-1]

def isPrime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    print(nthPrime(int(input().strip())))
