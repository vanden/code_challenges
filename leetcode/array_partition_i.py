# https://leetcode.com/submissions/detail/154254164/

# Simple, and in the spike of fastest runtimes, despite the O(nlogn). Not
# seeing how better is possible.

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(n for n in nums[::2])
