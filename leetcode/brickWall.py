# https://leetcode.com/problems/brick-wall/description/

# Broken

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        return len(wall) - self.bestJointCut(self._cuts(wall))
    
    def _cuts(self, wall):
        cuts = []
        for row in wall:
            runningSum = 0
            rowCuts = []
            for brick in row:
                runningSum += brick
                rowCuts.append(runningSum)
            cuts.append(rowCuts)
        return cuts
    
    def bestJointCut(self, cuts):
        best = -1
        for cutIndex in range(1, cuts[0][-1]):
            jointCount = 0
            for cut in cuts:
                if cutIndex in cut:
                    jointCount += 1
            best = max(best, jointCount)
        return best
