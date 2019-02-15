# https://leetcode.com/problems/find-the-duplicate-number/

# I spent a long time trying to figure out how to do this with O(1) space and
# without modifying the array. I broke down. I looked around and found an
# approach.

# Runtime: 24 ms, faster than 97.43% of Python online submissions for Find the
# Duplicate Number.

# Memory Usage: 8.3 MB, less than 73.53% of Python online submissions for Find
# the Duplicate Number.


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if hare == tortoise:
                break

        # Then the tortoise and the hare have the same value. But, this could
        # be either because that value is the repeated value, or because they
        # happened to have landed on it as part of the cycle and the repeat is
        # elsewhere.

        # But, as 0 not in the list, nothing can ever send to num[0]. So, if
        # two slow traversals come to agree, having started from different
        # points, they must have found duplicate values.

        turtle = nums[0]

        while turtle != tortoise:
            turtle = nums[turtle]
            tortoise = nums[tortoise]

        return turtle
