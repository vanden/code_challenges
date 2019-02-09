# https://leetcode.com/problems/largest-palindrome-product/description/

import itertools

class Solution:
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        upperBound = (10**n)-1
        lowerBound = 10**(n-1)
        for candidate in range(upperBound**2, (lowerBound-1)**2, -1):
            if not isPalindrome(candidate):
                continue

            for i in range(upperBound, lowerBound-1, -1):
                if candidate % i == 0:
                    if lowerBound < (candidate // i) < upperBound:
                        return candidate % 1337

    def isPalindrome(self, n):
        return n == int(''.join(reversed(str(n))))


s = Solution()
s.largestPalindrome(7)
