#https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            # # O(1) in space.
            # if k > len(nums)/2:
            #     # Then it is faster to do left rotations
            #     k = abs(len(nums) - k)
            #     for i in range(k):
            #         nums.append(nums.pop(0))
            # else:
            #     for i in range(k):
            #         nums.insert(0, nums.pop())


            # Fastest I know how to do, but O(n) in space
            nums[:] = nums[-k:] + nums[:-k]
# print()
# s = Solution()
# d = list(range(12))
# s.rotate(d, 5)
# print(d)
# d = list(range(12))
# s.rotate(d, 10)
# print(d)
