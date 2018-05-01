# https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set([n])
        while True:
            n = sum([int(d)**2 for d in list(str(n))])
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
