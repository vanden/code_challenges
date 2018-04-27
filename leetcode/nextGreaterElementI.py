# https://leetcode.com/problems/next-greater-element-i/description/


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result = []

        for num in nums1:
            for otherNum in nums2[nums2.index(num):]:
                if otherNum > num:
                    result.append(otherNum)
                    break
            else:
                result.append(-1)

        return result
