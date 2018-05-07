# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

# Given a sorted array consisting of only integers where every element appears
# twice except for one element which appears once. Find this single element
# that appears only once.

# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
# Input: [3,3,7,7,10,11,11]
# Output: 10

# So, at index i where i is odd, if the element at i is the same as at i -1,
# the missing element is to the right.
class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)//2
        if mid % 2 == 0:
            mid += 1
        print(mid, nums[mid-1:mid+2])

        if nums[mid] == nums[mid-1]:
            return self.singleNonDuplicate(nums[mid+1:])
        else:
            return self.singleNonDuplicate(nums[:mid])


# s = Solution()

# d = [1, 1, 2, 3, 3,]
# s.singleNonDuplicate(d)
