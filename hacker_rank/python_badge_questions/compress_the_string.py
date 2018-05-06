#https://www.hackerrank.com/challenges/compress-the-string/problem
import itertools

data = input()
result = []
for key, group in itertools.groupby(data):
    result.append((len(list(group)), int(key)))
print(' '.join((str(r) for r in result)))
