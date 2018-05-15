# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        # the simplest thing that could possibly work (and, not in the spirit
        # of the thing):
        #return min(nums)
        #
        # That turned out to beat 100% of Python3 solutions.


        # less against the spirit and not optimal for the overall idea:
        # for idx, num in enumerate(nums):
        #     try:
        #         if num > nums[idx+1]:
        #             return nums[idx+1]
        #     except IndexError:
        #         # Then it was the null-rotation
        #         return nums[0]
        # Also turns out to beat 100% of Py3 solutions.

        # But, let's optimize, anyway:

        left = 0
        right = len(nums) - 1

        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid
            else:
                right = mid

        return min(nums[left], nums[right])
