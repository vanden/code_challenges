# https://www.hackerrank.com/challenges/non-divisible-subset/problem

from collections import defaultdict

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    remainders = defaultdict(int)
    for el in S:
        remainders[el%k] += 1
    size = 0
    if remainders[0]:
        # Can only add one of them to S'
        size = 1
    complementPairs = []
    for val in remainders:
        if val:
            complement = k - val
            if not complement in remainders:
                # All can be added to S' as there are no conflicting elements
                size += remainders[val]
            elif complement == val:
                # The elements are self-complementary and we can add exactly 1
                # to S'
                size += 1
            elif complement < val:
                complementPairs.append((complement, val))
    for c, v in complementPairs:
        # For each subset S* and S** of values that pairwise conflict across
        # subsets, pick the larger subset.
        size += max(remainders[c], remainders[v])
    return size

def main():

    print(nonDivisibleSubset(5, [2, 7, 12, 17, 22]))

if __name__ == "__main__":
    main()
