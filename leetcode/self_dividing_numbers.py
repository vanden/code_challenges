#https://leetcode.com/problems/self-dividing-numbers/description/

class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        return [n for n in range(left, right+1) if self.isSelfDiver(n)]

    def isSelfDiver(self, n):
        digits = list(str(n))
        for digit in digits:
            if n == '0' or n % int(digit):
                return False
        return True
