# https://leetcode.com/problems/valid-perfect-square/description/


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        candidate = 1
        while True:
            testCase = candidate * candidate
            if testCase > num:
                break
            if testCase == num:
                return True
            candidate *= 2

        while True:
            candidate -= 1
            testCase = candidate * candidate
            if testCase == num:
                return True
            if testCase < num:
                return False
