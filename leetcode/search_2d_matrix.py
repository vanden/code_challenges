# https://leetcode.com/problems/search-a-2d-matrix/description/
class Solution:
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    def searchMatrix(self, matrix, target):

        if not matrix or not matrix[0]:
            # Edge case where 0 in [n, m]
            return False

        candidateRows = [row for row in matrix if row[0] <= target]
        if not candidateRows:
            return False

        # At most one row will remain
        candidateRows = [row for row in candidateRows if row[-1] >= target]
        if not candidateRows:
            return False

        return target in set(candidateRows[0])
