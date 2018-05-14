# https://leetcode.com/problems/largest-palindrome-product/description/

import itertools

class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        upperBound = 10**n-1
        lowerBound = 10**n

        # Naive thing without any effort at analysis of what a factor of a
        # palindrome must be like.
        #
        # Oh, but wait. This is dumb. Surely is is
        # better to start with the palidromic numbers and find one that
        # factors as desired. Still, let's run. I predict a timeout.

        # Indeed, for n = 7 run as a single test, it times out.
        largest = float('-inf')
        for x in range(upperBound, lowerBound-1, -1):
            for y in range(x, lowerBound-1, -1):
                if x*y <= largest:
                    break
                if self.isPalindrome(x * y):
                    largest = x * y
                    break
        return largest % 1337

    def isPalindrome(self, n):
        return n == int(''.join(reversed(str(n))))
