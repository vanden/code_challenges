# https://www.hackerrank.com/contests/projecteuler/challenges/euler025

fibs = [1, 1, 2, 3]

def indexOfLeastFibLenN(n):
    if len(str(fibs[-1])) >= n:
        for fib in fibs:
            if len(str(fib)) == n:
                return fibs.index(fib) + 1
    while True:
        nextFib = fibs[-1] + fibs[-2]
        fibs.append(nextFib)
        if len(str(nextFib)) == n:
            return fibs.index(nextFib) + 1


# caseCount = int(input())
# while caseCount:
#     caseCount -= 1
#     data = int(input())
#     print(indexOfLeastFibLenN(data))
    
