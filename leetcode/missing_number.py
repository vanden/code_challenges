# https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fullTotal = sum(range(len(nums)+1))
        return fullTotal - sum(nums)
