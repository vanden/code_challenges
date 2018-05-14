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

        for key in seen:
            if seen[key] == 1:
                return key
