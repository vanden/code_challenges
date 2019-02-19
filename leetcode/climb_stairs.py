# https://leetcode.com/problems/climbing-stairs/

# Runtime: 32 ms, faster than 100.00% of Python3 online submissions
# for Climbing Stairs.

# Memory Usage: 12.7 MB, less than 100.00% of Python3 online
# submissions for Climbing Stairs.


class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        totals = {0:1, 1:1}
        for i in range(2, n+1):
            totals[i] = totals[i-1] + totals[i-2]
            
        return totals[n]
