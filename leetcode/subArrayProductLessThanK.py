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
        for startIdx in range(len(nums)):
            offset = 0
            product = nums[startIdx]
            while product < k:                
                offset += 1
                count += 1
                if startIdx + offset >= len(nums):
                    break
                product = product * nums[startIdx + offset]
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
