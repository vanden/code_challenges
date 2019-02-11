# https://leetcode.com/problems/brick-wall/description/

from collections import defaultdict

# Before submitting, I wrote:
#
# I feel like this cannot be right as too simple. It does pass every test I
# know I failed (in that I got the output wrong), before
#
# and then:

# Runtime: 44 ms, faster than 90.54% of Python online submissions for Brick
# Wall.

# Memory Usage: 14.4 MB, less than 31.58% of Python online submissions for
# Brick Wall.


class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """

        joints = defaultdict(int)
        for row in wall:
            rowSum = 0
            for brick in row[:-1]:
                rowSum += brick
                joints[rowSum] += 1

        best = 0
        for v in joints.values():
            best = max(best, v)

        return len(wall) - best





cases = [
    ([[1], [1], [1]], 3),
    ([[2], [2], [2]], 3),
    ([[6], [6], [2, 4], [6], [1, 2, 2, 1], [6], [2, 1, 2, 1], [1, 5], [4, 1, 1],
      [1, 4, 1], [4, 2], [3, 3], [2, 2, 2], [5, 1], [5, 1], [6], [4, 2], [1, 5],
      [2, 3, 1], [4, 2], [1, 1, 4], [1, 3, 1, 1], [2, 3, 1], [3, 3], [3, 1, 1, 1],
      [3, 2, 1], [6], [3, 2, 1], [1, 5], [1, 4, 1]], 17),
    ([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]], 2),
]


if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        print(s.leastBricks(inPut) == outPut)
