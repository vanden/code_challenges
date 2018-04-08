#!/usr/bin/env python3
#https://leetcode.com/problems/reverse-string/description/

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]   # Fastest, but not in the spirit of the thing.
        #return ''.join(reversed(s))  # Fast, but still....
        # if not s:
        #     return s
        # index = -1
        # chars = []
        # while index > (len(s) * -1):
        #     chars.append(s[index])
        #     index -= 1

        # return ''.join(chars)
