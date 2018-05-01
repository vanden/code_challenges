#https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A Naive solution

        if not nums:
            return -1

        for idx, num in enumerate(nums):
            try:
                if sum(nums[:idx]) == sum(nums[idx+1]):
                    return idx
            except IndexError:
                break

        return -1
