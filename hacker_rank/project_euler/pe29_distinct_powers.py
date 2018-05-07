# https://www.hackerrank.com/contests/projecteuler/challenges/euler029

def distinctPowerCount(n):
    powers = set()
    for i in range(2, n+1):
        for j in range(i, n+1):
            powers.add(pow(i, j))
            powers.add(pow(j, i))

    return len(powers)

print(distinctPowerCount(int(input())))
