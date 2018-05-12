# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        candidates = [nums.pop()]
        if nums[0]*nums[1] > nums[-1] * nums[-2]:
            candidates.extend(nums[:2])
        else:
            candidates.extend(nums[-2:])

        return candidates[0] * candidates[1] * candidates[2]
