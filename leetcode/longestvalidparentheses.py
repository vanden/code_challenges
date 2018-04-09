#!/usr/bin/env python3

#https://leetcode.com/problems/longest-valid-parentheses/description/

# I believe that this works, but it times out on long inputs. It had 216 / 229 test cases passed before it timed out.

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if self.isBalanced(s):
            return len(s)
        substrings = self.getSubstrings(s)
        substrings = sorted(substrings, key=lambda x: -len(x))
        for sstring in substrings:
            if len(sstring) % 2:
                continue
            if self.isBalanced(sstring):
                return len(sstring)
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

    

    def getSubstrings(self, s):

        if len(s) == 0:
            return ['']
        elif len(s) == 1:
            return ['', s]
        seen = set()

        for length in range(len(s), 0, -1):
            for start in range(len(s)):
                if start + length > len(s):
                    break
                sstring = s[start:start + length]
                if sstring in seen:
                    continue
                seen.add(sstring)
                yield sstring
                               
        
# s = Solution()
# t = ")(((((()())()()))()(()))("
# print(s.longestValidParentheses(t))

#t = 'ababab'
# for ss in s.getSubstrings(t):
#     print(ss)

    
