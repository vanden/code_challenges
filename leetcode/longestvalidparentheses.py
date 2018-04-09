#!/usr/bin/env python3

#https://leetcode.com/problems/longest-valid-parentheses/description/

# Still too slow. Now, pass 217/229 cases.
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Restrict to substrings of even length as only they can be valid.
        startLength = int(len(s)/2) * 2

        for length in range(startLength, 0, -2):

            for start in range(0,len(s)-length+1):
                substring = s[start:start+length]
                if self.isBalanced(substring):
                    return len(substring)
        return 0

    def isBalanced(self, s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if not stack:
                    return False
                last = stack.pop()
                if last != '(':
                    return False
        return len(stack) == 0
