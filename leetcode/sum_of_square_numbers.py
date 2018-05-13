# https://leetcode.com/problems/sum-of-square-numbers/description/
import math

class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
#        if c < 3:
#            return True

#        bound = (c // 2) + 1  # Eliminating the name to squeeze ms

#        for i in range(0, int(math.sqrt(bound)) + 1):
# use of pow instead of math.sqrt seemed to make things slower, but it could be noise from the leetcode platform.
        for i in range(0, int(math.sqrt((c//2) + 1)) + 1):
            residue_root = math.sqrt(c - (i*i))
            if residue_root == int(residue_root):
                return True

        return False

# s = Solution()


# for i in range(23):
#     print(i, s.judgeSquareSum(i))

#print(20, s.judgeSquareSum(20))
