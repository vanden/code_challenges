# https://leetcode.com/problems/two-sum/

# Runtime: 36 ms, faster than 99.73% of Python3 online submissions for Two
# Sum.

# Memory Usage: 13.9 MB, less than 0.98% of Python3 online submissions for Two
# Sum.

class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':

        comps = {}

        for i, n in enumerate(nums):
            if n in comps:
                return comps[n], i
            comps[target - n] = i
