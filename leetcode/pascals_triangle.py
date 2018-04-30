# https://leetcode.com/problems/pascals-triangle/description/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        rows = [[1]]
        while len(rows) < numRows:
            new_row = [1,]
            for idx, item in enumerate(rows[-1][:-1]):
                new_row.append(item + rows[-1][idx+1])
            new_row.append(1)
            rows.append(new_row)
        return rows

s = Solution()
print(s.generate(6))
