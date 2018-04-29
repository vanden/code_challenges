#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(numbers):
            if target - num in numbers[idx+1:]:
                return [idx+1, numbers[idx+1:].index(target - num) + 2 + idx]


s = Solution()
print(s.twoSum([0,0,3,4], 0))
