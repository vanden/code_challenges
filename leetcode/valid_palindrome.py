# https://leetcode.com/problems/valid-palindrome/description/

# The fun recursive way timed out.

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c not in (
            ',', ';', '.', '!', '?', ':', "'", '"', '(', ')', '[', ']',
            '{', '}', ' ', '@', '#', '$', '%', '^', '&', '*', '-',
            '=', '+', '_', '<', '>', '/', '\\', '~', '`'))
        if len(s) < 2:
            return True
        return s = reversed(s)

s = Solution()
print(s.isPalindrome('fsdgetKLJHKJfgku;,.")({}'))
