#https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    print(a)
    swaps = 0
    done = False
    while not done:
        passSwaps, a = sortPass(a)
        if not passSwaps:
            done = True
        swaps += passSwaps
    print("Array is sorted in %s swaps." %swaps)
    print("First Element:", a[0])
    print("Last Element:", a[-1])

def sortPass(a):
    swaps = 0
    for i in range(0, len(a)-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swaps += 1
    return swaps, a

countSwaps([4, 2, 3, 1])
