#!/usr/bin/env python3

#https://leetcode.com/problems/longest-valid-parentheses/description/

# AGAIN, Still too slow. Still passing 217/229 cases.
class Solution:
    def longestValidParentheses(self, string):
        """
        :type s: str
        :rtype: int
        """
        # Restrict to substrings of even length as only they can be valid.
        startLength = int(len(string)/2) * 2

        # Length in descending order as once we find a valid string of a
        # length considered in that order, we know that we have found the
        # longest such string.
        for length in range(startLength, 0, -2):

            for start in range(0,len(string)-length+1):

                substring = string[start:start+length]
                parenCount = 0
                
                for c in substring:
                    if c == '(':
                        parenCount += 1
                    elif c == ')':
                        parenCount -= 1

                    if parenCount < 0:
                        break
                else:
                    if parenCount == 0:
                        return len(substring)
        return 0

# s = Solution()
# t = ")(((((()())()()))()(()))("
# #t = '(())))'
# print(s.longestValidParentheses(t))
