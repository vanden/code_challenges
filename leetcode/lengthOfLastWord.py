#!/usr/bin/env python3
#https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = [x for x in s.split(' ') if x.strip()]
        if not len(words):
            return 0
        return len(words[-1])
