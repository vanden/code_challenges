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
        n1 = list(reversed(nums1[:m]))
        nums2 = list(reversed(nums2[:n]))

        nums1.clear()

        while n1 and nums2:
            print(n1)
            print(nums2)
            if n1[-1] < nums2[-1]:
                nums1.append(n1.pop())
                print("n1")
            else:
                nums1.append(nums2.pop())
                print("nums2")
        nums1.extend(n1)
        nums1.extend(nums2)
        print(nums1)


s = Solution()
nums1 = [1,2,3,0,0,0]
s.merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
print(nums1)
        
#
# 3
# [2,5,6]
# 3
# Output:
# [1,2,2,3,6,5]
# Expected:
# [1,2,2,3,5,6]
