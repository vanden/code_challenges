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
        start = 0
        end = len(nums) - 1
        c = 0
        while start != end:
            mid = (start + end) // 2
            if mid % 2:
                if nums[mid] == nums[mid+1]:
                    # Then, unpaired is left
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] == nums[mid+1]:
                    # Unpaired right
                    start = mid
                else:
                    end = mid
        return nums[start]


s = Solution()
print()
d = [1, 2, 2, 3, 3,]
print(s.singleNonDuplicate(d))

d = [1, 1, 2, 3, 3,]
print(s.singleNonDuplicate(d))

d = [1, 1, 2, 2, 3,]
print(s.singleNonDuplicate(d))

print()

d = [1, 2, 2, 3, 3, 4, 4]
print(s.singleNonDuplicate(d))

d = [1, 1, 2, 3, 3, 4, 4]
print(s.singleNonDuplicate(d))

d = [1, 1, 2, 2, 3, 4, 4]
print(s.singleNonDuplicate(d))

d = [1, 1, 2, 2, 3, 3, 4]
print(s.singleNonDuplicate(d))

