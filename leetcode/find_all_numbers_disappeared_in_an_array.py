# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = list(range(1, len(nums) + 1))

        for num in nums:
            missing[num-1] = 0

        return [m for m in missing if m]
