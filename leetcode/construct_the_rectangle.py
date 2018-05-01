# https://leetcode.com/problems/construct-the-rectangle/description/

from math import sqrt

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        start = int(sqrt(area))
        for length in range(start, 0, -1):
            if not area % length:
                return sorted([area/length, length], reverse=True)


s = Solution()
# on leetcode, this timed out. Max value to consider is 10000000
print(s.constructRectangle(9999991))
