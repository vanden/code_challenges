# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

import itertools

length = int(input())
data = input().split(' ')
k = int(input())
acount = 0
scount = 0
for sample in itertools.combinations(range(length), k):
    scount += 1
    for index in sample:
        if data[index] == 'a':
            acount += 1
            break
print(acount/scount)
