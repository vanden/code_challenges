# https://leetcode.com/problems/single-number-ii/description/

import collections

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = collections.defaultdict(int)
        for num in nums:
            seen[num] += 1

        return min(seen.keys(), key=lambda n: seen[n])
