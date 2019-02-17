# https://leetcode.com/problems/delete-and-earn/submissions/

# Runtime: 152 ms, faster than 22.26% of Python3 online submissions
# for Delete and Earn.

# Memory Usage: 12.4 MB, less than 100.00% of Python3 online
# submissions for Delete and Earn.


class Solution:
    def deleteAndEarn(self, nums: 'List[int]') -> 'int':
        if not nums:
            return 0
        nums.sort()
        # Reduce to houserobber
        
        # Something more efficient must be possible
        
        points = []
        for i in range(nums[0], nums[-1]+1):
            points.append(i * nums.count(i))
        if len(points) < 3:
            return max(points)
        memo = {-1:0,0:points[0]}
        for i in range(1, len(points)):
            memo[i] = max(memo[i-2]+points[i], memo[i-1])
        return memo[len(points)-1]
