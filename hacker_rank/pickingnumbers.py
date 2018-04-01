#!/bin/python3

# https://www.hackerrank.com/challenges/picking-numbers/problem


# This cannot be an optimal solution.

def pickingNumbers(a):
    filtered = []
    for num in a:
        if num-1 in a or num+1 in a:
            filtered.append(num)
    
    nums = sorted(list(set(filtered)))

    # Can't restrict to filtered as a single value that occurs many times
    # might be the relevant "pair"
    maxval = max([a.count(x) for x in a])
    # A possible improvement: store a counts dict; that way, the two counts in
    # each iteration of the loop below will be quick.

    
    higher_count = 0
    for (lower, higher) in zip(nums[0:-1], nums[1:]):
        if higher - lower > 1:
            continue
        lower_count = filtered.count(lower)
        higher_count = filtered.count(higher)
        if lower_count + higher_count  > maxval:
            maxval = lower_count + higher_count
    return maxval

    
        

def tests():
      """
      >>> data = [4, 6, 5, 3, 3, 1]; pickingNumbers(data)
      3
      >>> data = [1, 2, 2, 3, 1, 2]; pickingNumbers(data)
      5
      >>> data =  [4, 2, 3, 4, 4, 9, 98, 98, 3, 3, 3, 4, 2, 98, 1, 98, 98, 1, 1, 4, 98, 2, 98, 3, 9, 9, 3, 1, 4, 1, 98, 9, 9, 2, 9, 4, 2, 2, 9, 98, 4, 98, 1, 3, 4, 9, 1, 98, 98, 4, 2, 3, 98, 98, 1, 99, 9, 98, 98, 3, 98, 98, 4, 98, 2, 98, 4, 2, 1, 1, 9, 2, 4]; pickingNumbers(data)
      22
      >>> data = [66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]; pickingNumbers(data)
      100
      >>> data = [7, 12, 13, 19, 17, 7, 3, 18, 9, 18, 13, 12, 3, 13, 7, 9, 18, 9, 18, 9, 13, 18, 13, 13, 18, 18, 17, 17, 13, 3, 12, 13, 19, 17, 19, 12, 18, 13, 7, 3, 3, 12, 7, 13, 7, 3, 17, 9, 13, 13, 13, 12, 18, 18, 9, 7, 19, 17, 13, 18, 19, 9, 18, 18, 18, 19, 17, 7, 12, 3, 13, 19, 12, 3, 9, 17, 13, 19, 12, 18, 13, 18, 18, 18, 17, 13, 3, 18, 19, 7, 12, 9, 18, 3, 13, 13, 9, 7]; pickingNumbers(data)
      30
      """
      
      
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
