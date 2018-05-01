# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Likely too slow
        missing = []
        for i in range(1, len(nums)+1):
            if i not in nums:
                missing.append(i)

        return missing
