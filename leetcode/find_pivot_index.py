#https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # A less Naive solution

        if not nums:
            return -1

        left_sum = 0
        right_sum = sum(nums) - nums[0]

        for idx, num in enumerate(nums):
            if left_sum == right_sum:
                return idx

            left_sum += num
            try:
                right_sum -= nums[idx+1]
            except IndexError:
                return -1
