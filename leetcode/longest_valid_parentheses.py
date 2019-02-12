#!/usr/bin/env python3

#https://leetcode.com/problems/longest-valid-parentheses/description/

# *AGAIN*, Still too slow. Still passing 227/229 cases.
class SolutionOld:
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


# OK, I was close, before.
#
# One thing that immediately seems like it might help is to start by striping
# all ')' from the front and '(' from the back.
#
# But, that's a small help. The obvious issue is the above is O(n2) and
# chipping a bit off of n isn't going to help, really.
#
# However, we can strip, then find the longest initial substring that is
# valid. Then, recurse on the rest, comparing the recursed value to the
# initial value and returning whichever is best.
#
# That's a plan, but only the outline of the code.
#
# And, now that I consider cases like "()()() ( ()()" and "()()() ( ()()()()",
# I see that is still going to be O(n2). Damn.
#
#


# So, it passed, but is sloooow.

# Unhappy.

# Runtime: 14204 ms, faster than 0.94% of Python online submissions for
# Longest Valid Parentheses.

# Memory Usage: 417.6 MB, less than 0.95% of Python online submissions for
# Longest Valid Parentheses.

class Solution:
    def longestValidParentheses(self, string):
        string = string.lstrip(')').rstrip('(')
        if not string:
            return 0

        # We now are certain we have a non-empty string, starting with '('.

        unclosedCount = 0
        balancedIndices =[]
        for i, p in enumerate(string):
            if p == '(':
                unclosedCount += 1
            else:
                unclosedCount -= 1
                if unclosedCount == 0:
                    balancedIndices.append(i)
            if unclosedCount < 0:
                break
        if not balancedIndices:
            if unclosedCount == 0:
                initialLength = len(string)-1
            else:
                initialLength = 0
        else:
            initialLength = max(balancedIndices)

        trailingLength = self.longestValidParentheses(string[max(1, initialLength):])

        return max(initialLength + 1, trailingLength)


cases = [
    ("((((((", 0),
    ("(((()((", 2),
    (")()())", 4),
    ("()())", 4),
    ("()()", 4),
    ("(", 0),
    ("())", 2),
    ("()()()(", 6),
    ("()()()(()()", 6),
    ("()()()(()()()()", 8),
    ("()()()(())()()()", 16),
    ("()()()((())()()()", 10),
    ("()()()()())()()()", 10),
]

if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        result = s.longestValidParentheses(inPut)
        if result == outPut:
            print(True)
        else:
            print(result == outPut, result, outPut, inPut)
