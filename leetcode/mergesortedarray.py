# https://leetcode.com/problems/merge-sorted-array/description/

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        n1Index = 0
        while len(nums1) > m:
            nums1.pop()
        for num in nums2:

            while n1Index < len(nums1) and nums1[n1Index] <= num:
                n1Index += 1
            if n1Index > len(nums1):
                nums1.append(num)
            else:
                nums1.insert(n1Index, num)



s = Solution()
nums1 = [1,2,3,0,0,0]
s.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
