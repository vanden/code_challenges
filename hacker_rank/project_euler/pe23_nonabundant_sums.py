#https://www.hackerrank.com/contests/projecteuler/challenges/euler023

import math

def properDivisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            if i > 1:
                divisors.add(int(n/i))
    return divisors

abundantNums = set()
checked = set()

def isAbundant(n):
    if n in abundantNums:
        return True
    if n in checked:
        return False
    checked.add(n)
    if sum(properDivisors(n)) > n:
        abundantNums.add(n)
        return True
    return False

def expressibleAsSumOfAbundantPairs(n):
    for i in range(12, max(int((n-12)/2)+6, 13)):
        if isAbundant(i):
            if isAbundant(n-i):
                print("YES")
                return
    print("NO")

caseCount = int(input())

while caseCount:
    caseCount -= 1
    n = int(input())
    #print(n)
    expressibleAsSumOfAbundantPairs(n)
    
