# https://leetcode.com/problems/set-mismatch/description/
class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        correctSum = sum(range(1, len(nums)+1))
        dedupedSum = sum(set(nums))
        actualSum = sum(nums)

        missing = correctSum - dedupedSum
        dupe = actualSum - dedupedSum

        return [dupe, missing]
