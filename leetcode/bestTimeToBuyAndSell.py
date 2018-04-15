#!/usr/bin/env python3
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = float("-inf")
        lowest = float("inf")

        for price in prices:
            if price - lowest > best:
                best = price - lowest
            if lowest > price:
                lowest = price

        return max(best, 0)

if __name__ == '__main__':
    s = Solution()
    test = [7,1,5,3,6,4]
    print(s.maxProfit(test))
    

    test = [7,6,4,3,1]
    print(s.maxProfit(test))
