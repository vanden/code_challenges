# https://leetcode.com/problems/word-pattern/description/

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(' ')
        if len(words) != len(pattern):
            return False
        
        components = []
        for c in pattern:
            if c not in components:
                components.append(c)
        elements = {}

        for component in components:
            idx = pattern.index(component)
            elements[component] = words[idx]

        if len(elements) != len(set(elements.values())):
            return False
                                
        for idx, component in enumerate(pattern):
            if elements[component] != words[idx]:
                return False

        return True


s = Solution()
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("deadbeef", "d e a d b e e f"))
#{'a': 'd', 'b': 'e', 'd': 'a', 'e': 'd', 'f': 'b'}
