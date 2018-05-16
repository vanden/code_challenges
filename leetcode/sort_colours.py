# https://leetcode.com/problems/sort-colors/description/

# Ugly, complex, and fast: 36ms beating 100% of Py3 solutions

class Solution:
    def swap(self, nums, idx1, idx2):
        nums[idx1], nums[idx2] = nums[idx2], nums[idx1]

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        lastZeroIdx = None
        firstOneIdx = None
        placeForTwoIdx = -1

        idx = 0

        while idx < len(nums):

            if nums[idx] == 0:

                if lastZeroIdx is None:
                    self.swap(nums, 0, idx)
                    lastZeroIdx = 0
                    idx += 1
                    if firstOneIdx is not None:
                        firstOneIdx = 1
                else:
                    if lastZeroIdx == idx - 1:
                        lastZeroIdx = idx
                        idx += 1
                    else:
                        self.swap(nums, lastZeroIdx+1, idx)
                        lastZeroIdx += 1
                        firstOneIdx += 1

            elif nums[idx] == 1:
                # Since we have moved all 0s left and 2s right, this
                # has to be the last 1 in the central run of 1s.

                if firstOneIdx is None:
                    firstOneIdx = idx
                idx += 1

            elif nums[idx] == 2:
                self.swap(nums, placeForTwoIdx, idx)
                placeForTwoIdx -= 1
            if idx + abs(placeForTwoIdx) == len(nums) + 1 or idx == placeForTwoIdx:
                break

        if nums[-1] == 0 and firstOneIdx is not None:
            # This can be needed if there are no 2s in the input
            self.swap(nums, firstOneIdx, -1)


s = Solution()
nums = [1, 2, 1, 2, 0, 1, 0, 2, 0, 2, 1, 1, 0]
#nums = [1, 0, 1, 0]
#nums = [0, 0]
#nums = [2, 0, 1]
s.sortColors(nums)
print(nums)
