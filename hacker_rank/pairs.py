# https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

def pairs(k, arr):
    if k == 0:
        return len(arr)
    vals = set()
    total = 0
    for el in arr:
        vals.add(el)
        total += el - k  in vals
        total += el + k in vals
    return total
