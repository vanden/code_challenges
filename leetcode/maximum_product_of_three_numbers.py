# https://leetcode.com/problems/maximum-product-of-three-numbers/description/

# Uglier than the sorting version. But, somewhat simpler and O(n) and O(1)
# rather than O(nlogn) and O(n). (I think the sorting version is O(n) because
# while the input nums got replaced by the sorted version, the caller would
# still retain a reference, so there was a new O(n) memory allocation.



class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        min1, min2 = float('inf'), float('inf')

        for num in nums:
            if num < min2 and num >= min1:
                min2 = num
            elif num < min1:
                min2 = min1
                min1 = num
            if num > max3 and num <= max2:
                max3 = num
            elif num > max2 and num <= max1:
                max3 = max2
                max2 = num
            elif num > max1:
                max3 = max2
                max2 = max1
                max1 = num
        return max(max1 * min1 * min2, max1 * max2 * max3)

# d = [1,2,3,2]
# s = Solution()
# print(s.maximumProduct(d))
