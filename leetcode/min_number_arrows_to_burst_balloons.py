# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, reverse=True, key=lambda point: point[-1])
        arrowCount = 0
        while points:
            point = points.pop()
            arrowX = point[-1]
            arrowCount += 1
            while points and points[-1][0] <= arrowX:
                points.pop()
        return arrowCount
