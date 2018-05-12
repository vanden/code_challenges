# https://leetcode.com/problems/elimination-game/description/

class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        ints = list(range(1, n+1))

        while len(ints) > 1:
            for i in reversed(range(0, len(ints), 2)):
                ints.pop(i)
            if len(ints) == 1:
                break
            for i in range(len(ints)-1, -1, -2):
                ints.pop(i)

        return ints[0]

# Unsurprisingly, this is too slow:
# 3162 / 3377 test cases passed.
# Status: Time Limit Exceeded
# Last executed input:
# 7068
