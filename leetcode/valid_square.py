# https://leetcode.com/problems/valid-square/description/

class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        pts = sorted((x, y) for [x, y] in [p1, p2, p3, p4])
        if len(set(pts)) != 4:
            return False
        distance = self.dist(pts[0], pts[1])
        for side in [(pts[1], pts[3]), (pts[0], pts[2]),
                     (pts[2], pts[3])]:
            pt1, pt2 = side
            if self.dist(pt1, pt2) != distance:
                return False
        return int(self.dist(pts[0], pts[3]) * 10**5) == int(10**5 * distance * 2**0.5)

    def dist(self, p1, p2):
        xdist = p1[0] - p2[0]
        ydist = p1[1] - p2[1]
        return (xdist**2 + ydist**2)**0.5

p1 = [1,0]
p2 = [-1,0]
p3 = [0,1]
p4 = [0,-1]
s = Solution()
print(s.validSquare(p1, p2, p3, p4))

p1 = [1,1]
p2 = [5,3]
p3 = [3,5]
p4 = [7,7]
# print(sorted((p1, p2, p3, p4)))
# print(s.validSquare(p1, p2, p3, p4))    
