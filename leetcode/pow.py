#!/usr/bin/env python3
#https://leetcode.com/problems/powx-n/description/

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if not n % 2:
            return self.myPow(x*x, n/2)
        return x * self.myPow(x, n-1)
