# https://leetcode.com/problems/move-zeroes/

# Runtime: 44 ms, faster than 99.90% of Python3 online submissions for Move
# Zeroes.

# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for
# Move Zeroes.

class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return

        slow = 0
        fast = 1

        while slow < length and fast < length:
            if nums[fast] == 0:
                fast += 1
                continue

            if nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            if fast == slow + 1:
                fast += 1
            slow += 1


if __name__ == "__main__":
    s = Solution()
    cases = [
        [4, 2, 4, 0, 0, 3, 0, 5, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        ]

    for numList in cases:
        s.moveZeroes(numList)
        print(numList)
