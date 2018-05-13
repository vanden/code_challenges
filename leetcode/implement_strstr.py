# https://leetcode.com/problems/implement-strstr/description/

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

#        Not in the spirit of the thing
#        return haystack.find(needle)

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
