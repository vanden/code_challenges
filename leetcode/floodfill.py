#!/usr/bin/env python3
# https://leetcode.com/problems/flood-fill/description/


class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        offsets = [(1,0), (0,1), (-1,0), (0, -1)]
        pixelsToExplore = [(sr, sc)]
        origColor = image[sr][sc]
        if origColor == newColor:
            return image
        image[sr][sc] = newColor
        
        while pixelsToExplore:
            (y, x) = pixelsToExplore.pop()
            for (dx, dy) in offsets:
                ny = y + dy
                nx = x + dx
                if ny > -1 and nx > -1 and ny < len(image) and nx < len(image[0]):
                    if image[ny][nx] == origColor:
                        image[ny][nx] = newColor
                        pixelsToExplore.append((ny, nx))
        return image

# image = [[1,1,1],[1,1,0],[1,0,1]]
# y = 1
# x = 1
# newC = 2

# print(floodFill(image, y, x, newC))
