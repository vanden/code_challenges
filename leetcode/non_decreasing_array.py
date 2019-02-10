# https://leetcode.com/problems/non-decreasing-array/

# If we scan an array and find there has been a decrease from a[i-1] to a[i]
# (i.e., a[i-1] > a[i]), there are two possible patches:
#
# 1) Remove a[i-1]
# 2) Remove a[i]
#
# (1) will fail if a[i-2] > a[i]
# (2) will fail if a[i-1] > a[i+1]
#
# Assuming that neither failure clause occurs, (1) and (2) will both fail if
# the remaining array has another decreasing pair. That is to say, in case
# (1), if a[i:] has a decrease and, in case (2), if a[i+1:] has a decrease.
#
# This doesn't seem likely to be the optimal strategy, though.

# And, it was not. This one took WAAAY to much effort!

# I never managed to get the fussy details of the above strategy to work. I'm
# pretty sure it would have timed-out, though, as it was rather naive.

# Runtime: 32 ms, faster than 100.00% of Python online submissions for
# Non-decreasing Array.

# Memory Usage: 7.8 MB, less than 94.63% of Python online submissions for
# Non-decreasing Array.


class Solution():
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True

        decreaseIndex = None

        for i, num in enumerate(nums[:-1]):
            if num > nums[i+1]:
                if not decreaseIndex is None:
                    return False
                decreaseIndex = i

        if not decreaseIndex: # Covers None and 0
            return True

        if len(nums[decreaseIndex:]) < 3:
            return True

        if nums[decreaseIndex-1] <= nums[decreaseIndex+1]:
            return True

        return nums[decreaseIndex] <= nums[decreaseIndex+2]




cases = [
    ([1,], True),
    ([42, 1], True),
    ([2, 3, 3, 2, 4], True),
    ([4, 2, 3], True),
    ([3,4,2,3], False),
    ([4, 5, 1], True),
    ([4, 2, 1], False),
    ([1, 1, 1,], True),
    ([0, 1, 2, 3, 4, 5], True),
    ([0, 1, 2, 3, 2, 5], True),
    ([0, 1, 2, 1, 3, 4, 3], False),
    ([1,2,5,4,3], False),
    ]

if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        print(s.checkPossibility(inPut)==outPut)


# [2,3,3,2,4]
# [4,2,3]
# [4,2,1]
# [1,1,1]
# [0,1,2,3,4,5]
# [0,1,2,3,2,5]
