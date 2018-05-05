# https://www.hackerrank.com/challenges/angry-professor/problem

import sys

def angryProfessor(k, a):
    if len([t for t in a if t <= 0]) >= k:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        a = list(map(int, input().strip().split(' ')))
        result = angryProfessor(k, a)
        print(result)
