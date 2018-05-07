# https://www.hackerrank.com/contests/projecteuler/challenges/euler020

factorials = {0:1, 1:1, 2:2, 3:6}


def factorial(n):
    for i in range(4, n+1):
        if factorials.get(i):
            continue
        else:
            factorials[i] = factorials[i-1] * i
    return factorials[n]

def factorialDigitSum(n):
    return sum(int(x) for x in str(factorial(n)))

#print(factorial(6))

caseCount = int(input())
while caseCount:
    caseCount -= 1
    print(factorialDigitSum(int(input())))
