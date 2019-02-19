# https://leetcode.com/problems/min-cost-climbing-stairs/

# Runtime: 48 ms, faster than 70.32% of Python3 online submissions for
# Min Cost Climbing Stairs.

# Memory Usage: 12.6 MB, less than 100.00% of Python3 online
# submissions for Min Cost Climbing Stairs.

class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> 'int':

        if len(cost) < 3:
            return min(cost)
        
        totalCosts = [0,0]
        
        for i in range(2, len(cost)):
            totalCosts.append(min(
                (totalCosts[i-1] + cost[i-1]),
                (totalCosts[i-2] + cost[i-2])))
            
        return min((totalCosts[-1] + cost[-1]),
                   (totalCosts[-2] + cost[-2]))
