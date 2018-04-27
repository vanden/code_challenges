#https://leetcode.com/problems/couples-holding-hands/description/

class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        swapCount = 0
        for index, person in enumerate(row):
            if index == len(row) -1:
                continue
            if person % 2:
                swapIndex = row.index(person-1)
            else:
                # even case
                swapIndex = row.index(person+1)

            if swapIndex <= index + 1:
                continue
            else:
                row[index+1], row[swapIndex] = row[swapIndex], row[index+1]
                swapCount += 1

        return swapCount
