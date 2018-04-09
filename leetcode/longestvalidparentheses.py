#!/usr/bin/env python3

#https://leetcode.com/problems/longest-valid-parentheses/description/

# *AGAIN*, Still too slow. Still passing 227/229 cases.
class Solution:
    def longestValidParentheses(self, string):
        """
        :type s: str
        :rtype: int
        """
        maxLen = 0
        for start in range(len(string)):
            if (len(string) - start) < maxLen:
                return maxLen
            index = start
            parenCount = 0
            while index < len(string):
                if string[index] == '(':
                    parenCount += 1
                else:
                    parenCount -= 1
                if parenCount < 0:
                    break
                if parenCount == 0:
                    maxLen = max(maxLen, index - start + 1)
                index += 1
        return maxLen

#s = Solution()
#t = ")(((((()())()()))()(()))("
# #t = '(())))'
#print(s.longestValidParentheses(t))
