# https://leetcode.com/problems/find-the-difference/submissions/1

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sCounts = collections.defaultdict(int)
        tCounts = collections.defaultdict(int)
        for c in s:
            sCounts[c] += 1
        for c in t:
            tCounts[c] += 1
        for c in tCounts:
            if c not in sCounts or tCounts[c] > sCounts[c]:
                return c
