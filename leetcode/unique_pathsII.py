# https://leetcode.com/problems/unique-paths-ii/

# Runtime: 36 ms, faster than 98.88% of Python3 online submissions for
# Unique Paths II.

# Memory Usage: 12.5 MB, less than 100.00% of Python3 online
# submissions for Unique Paths II.

from collections import defaultdict

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        
        memo = {-1: defaultdict(int)}

        for rIdx in range(len(obstacleGrid)):
            
            memo[rIdx] = defaultdict(int)
        
            for cIdx in range(len(obstacleGrid[rIdx])):
            
                if obstacleGrid[rIdx][cIdx]:
                    continue
                
                memo[rIdx][cIdx] = memo[rIdx-1][cIdx] + memo[rIdx][cIdx-1]
                
        return memo[len(obstacleGrid)-1][len(obstacleGrid[0])-1]
                
                
                
