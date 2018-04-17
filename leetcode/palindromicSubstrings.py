#!/usr/bin/env python3
#https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        if not s:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):

            odd_viable = True
            even_viable = True
            
            for j in range(min(i, len(s) - i) + 1):
                 # The bounds to ensure we don't go off the edges of the string
                if not(odd_viable or even_viable):
                    break

                if odd_viable:
                    # odd length string
                    oddString = s[i-j:i+j+1]
                    if len(oddString)%2 and oddString[0] == oddString[-1]:
                        count+=1
                    else:
                        odd_viable = False
                if even_viable:
                    evenString = s[i-j:i+j]
                    if not evenString:
                        continue
                    if evenString[0] == evenString[-1]:
                        count += 1
                    else:
                        odd_viable = False
                        
        return count

def tests():
    """
    >>> s = Solution()
    >>> s.countSubstrings("abc")
    3
    >>> s.countSubstrings("aaa")
    6
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    s = Solution()
    s.countSubstrings("abc")
