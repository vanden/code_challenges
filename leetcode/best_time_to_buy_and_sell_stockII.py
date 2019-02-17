# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

# Runtime: 40 ms, faster than 99.28% of Python3 online submissions for
# Best Time to Buy and Sell Stock II.

# Memory Usage: 12.9 MB, less than 100.00% of Python3 online
# submissions for Best Time to Buy and Sell Stock II.

class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        profit = 0
        if len(prices) < 2:
            return profit
        
        # We can avoid much complexity in trying to find the optimal
        # duration to hold on to any purchase by treating a purchase
        # over prices like [1,2,7,1] not as trying to figure out if we
        # should sell at 2 or at 7, but by just saying we sell at 2
        # and then immediately buy at 2, again.

        for i in range(1, len(prices)):
            last, now = prices[i-1], prices[i]
            if last < now:
                profit += now - last

        return profit
