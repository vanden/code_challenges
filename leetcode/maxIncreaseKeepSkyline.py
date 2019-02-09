# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/


class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [max(row) for row in grid]

        col_maxes = []
        for colIdx in range(len(grid[0])):
            col = [grid[row][colIdx] for row in range(len(grid))]
            col_maxes.append(max(col))

        # print(row_maxes, col_maxes)
        increases = 0
        for idx, row in enumerate(grid):
            for jdx, height in enumerate(row):
                increases += min(row_maxes[idx], col_maxes[jdx]) - height
        return increases


# grid =[ [3, 0, 8, 4],
#         [2, 4, 5, 7],
#         [9, 2, 6, 3],
#         [0, 3, 1, 0] ]

# s = Solution()
# s.maxIncreaseKeepingSkyline(grid)
