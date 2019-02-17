# https://leetcode.com/problems/house-robber/submissions/

# Runtime: 32 ms, faster than 100.00% of Python3 online submissions
# for House Robber.

# Memory Usage: 12.5 MB, less than 100.00% of Python3 online
# submissions for House Robber.


class Solution:
    def rob(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        memo = {-1:0, 0:nums[0]}
        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])
        return memo[len(nums)-1]
