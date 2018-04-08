#!/usr/bin/env python3
#https://leetcode.com/problems/keyboard-row/description/

# Stunningly, this was in the fastest group for Python3; not my normal result!

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')

        result = []
        
        for word in words:
            chars = set(word.lower())
            print(chars)
            if (chars.issubset(row1) or chars.issubset(row2) or
                chars.issubset(row3)):
                result.append(word)

        return result

