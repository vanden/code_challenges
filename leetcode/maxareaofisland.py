#!/usr/bin/env python3
#https://leetcode.com/problems/max-area-of-island/description/

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        offsets = [(1,0), (0,1), (-1,0), (0,-1)]
        areas = []
        inIsland = False
        toExplore = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    area = 1
                    grid[y][x] = '#'
                    toExplore = [(y, x)]
                    while toExplore:
                        y, x = toExplore.pop()
                        for (dy, dx) in offsets:
                            ny, nx = y + dy, x + dx
                            if (ny < 0 or nx < 0 or
                                ny >= len(grid) or nx >= len(grid[0])):
                                continue
                            if grid[ny][nx] == 1:
                                grid[ny][nx] = '#'
                                area += 1
                                toExplore.append((ny, nx))
                    areas.append(area)
        if not areas:
            return 0
        return max(areas)
