#!/usr/bin/env python3
#https://leetcode.com/problems/jewels-and-stones/description/

from collections import defaultdict

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # Simple and slow:
        # jewels = 0
        # for c in J:
        #     jewels += S.count(c)

        # return jewels

        counts = defaultdict(int)
        for c in S:
            counts[c] += 1

        return sum(counts[c] for c in J)
