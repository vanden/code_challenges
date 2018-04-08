class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matches = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            if c in ')}]':
                if not stack:
                    return False
                last = stack.pop()
                if c != matches[last]:
                    return False
        if stack:
            return False
        else:
            return True
