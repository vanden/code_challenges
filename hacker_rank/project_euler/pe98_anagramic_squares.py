#https://www.hackerrank.com/contests/projecteuler/challenges/euler098

import collections
#import datetime

def boundsForNDigitSquares(n):
    return int((10**(n-1))**0.5)+1, int(((10**n)-1)**0.5)

def normalForm(n):
    return int(''.join(sorted([c for c in str(n)])))

def anagramicSquaresOfNDigits(n):
    anagramicSquares = collections.defaultdict(list)
    low, high = boundsForNDigitSquares(n)
    for i in range(low, high+1):
        square = i*i
        anagramicSquares[normalForm(square)].append(square)

    return anagramicSquares

def largestAnagramicSquareSetRep(n):
    anagramicSquares = anagramicSquaresOfNDigits(n)

    longestLength = 0
    longestAnagramicSets = []

    for key in anagramicSquares:
        squares = sorted(anagramicSquares[key])
        if len(squares) == longestLength:
            longestAnagramicSets.append(squares)
        elif len(squares) > longestLength:
            longestLength = len(squares)
            longestAnagramicSets = [squares]

    square = -1
    for squares in longestAnagramicSets:
        if squares[-1] > square:
            square = squares[-1]
    return square

#start = datetime.datetime.now()
#print(boundsForNDigitSquares(2))
print(largestAnagramicSquareSetRep(5))
#print(datetime.datetime.now()-start)
