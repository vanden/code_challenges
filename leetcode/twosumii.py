#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = set(numbers)
        for num in nums:
            if target - num in nums:
                low, high = (sorted([numbers.index(num) + 1, numbers.index(target - num) + 1]))
                if low == high:
                    high += 1
                return [low, high]


s = Solution()
print(s.twoSum([0,0,3,4], 0))
