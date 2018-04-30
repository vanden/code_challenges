# https://leetcode.com/problems/pascals-triangle-ii/description/

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        last_row = [1, 1]
        for _ in range(2, rowIndex+1):
            new_row = [1,]
            for idx, __ in enumerate(last_row[:-1]):
                new_row.append(last_row[idx] + last_row[idx+1])
            new_row.append(1)
            last_row = new_row
        return new_row
