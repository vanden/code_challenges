# https://leetcode.com/problems/perfect-number/description/

class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        divisors = self.divisors(num)
        divisors.discard(num)
        return num == sum(divisors)

    def divisors(self, num):
        divisors = set()
        for i in range(1, int(pow(num, 0.5)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num/i)

        return divisors
