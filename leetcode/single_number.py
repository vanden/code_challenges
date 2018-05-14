# https://leetcode.com/problems/single-number/description/

import collections

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Works, and is in the huge spike of solutions at the fast end. But, O(n) space.
        seen = collections.defaultdict(int)
        for num in nums:
            seen[num] += 1

        # for key in seen:
        #     if seen[key] == 1:
        #         return key

        for k, v in seen.items():
            if v == 1:
                return k

        # The problem spec doesn't give the needed guarantees for this to
        # work, but let's see. And, indeed, there are test cases for which it
        # fails.
        #
        # for num in nums:
        #     nums[abs(num)-1] *= -1
        # for num in nums:
        #     if nums[abs(num)-1] < 0:
        #         return abs(num)
