# https://leetcode.com/problems/third-maximum-number/description/

# It isn't pretty. But, it is O(n) in time and O(1) in space. On at least one
# submission, it was faster than all other Python submissions.
#
# If there was no worry about space, it would make sense to do `nums =
# set(nums)'. Then the entire mazes stuff could go away.

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 4:
            if len(set(nums)) == 3:
                return min(nums)
            else:
                return max(nums)

        max1, max2, max3 = [float('-inf')] * 3
        maxes = set()
        for num in nums:
            if num in maxes:
                continue
            if num > max1:
                maxes.discard(max3)
                maxes.add(num)
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                maxes.discard(max3)
                maxes.add(num)
                max3 = max2
                max2 = num
            elif num > max3:
                maxes.discard(max3)
                maxes.add(num)
                max3 = num
        if len(maxes) < 3:
            return max(maxes)
        return max3
