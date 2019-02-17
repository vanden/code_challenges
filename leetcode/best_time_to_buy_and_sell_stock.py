#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# Runtime: 40 ms, faster than 99.57% of Python3 online submissions for
# Best Time to Buy and Sell Stock.

# Memory Usage: 12.8 MB, less than 100.00% of Python3 online
# submissions for Best Time to Buy and Sell Stock.


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bestProfit = float("-inf")
        lowest = float("inf")

        for price in prices:
            if price - lowest > bestProfit:
                bestProfit = price - lowest
            if lowest > price:
                lowest = price

        return max(bestProfit, 0)

if __name__ == '__main__':
    s = Solution()
    test = [7,1,5,3,6,4]
    print(s.maxProfit(test))
    

    test = [7,6,4,3,1]
    print(s.maxProfit(test))
