#!/usr/bin/env python3
#https://leetcode.com/problems/subarray-product-less-than-k/description/

from functools import reduce

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            product = float("-inf")
            for j in range(i+1, len(nums)+1):
                product = reduce(lambda x,y: x*y, nums[i:j])
                if product < k:
                    count += 1
                else:
                    break
        return count


def test():
    """
    >>> s = Solution()
    >>> nums, k = [10, 5, 2, 6], 100
    >>> s.numSubarrayProductLessThanK(nums, k)
    8
    """
if __name__ == "__main__":
    import doctest        
    doctest.testmod(optionflags=doctest.ELLIPSIS)
