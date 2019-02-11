#!/usr/bin/env python3
#https://leetcode.com/problems/palindromic-substrings/description/

# This feels to be a cheat, as I am special casing trailing substrings with a
# single letter.

# Runtime: 328 ms, faster than 43.86% of Python3 online submissions for
# Palindromic Substrings.

# Memory Usage: 12.5 MB, less than 36.44% of Python3 online submissions for
# Palindromic Substrings.

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        count = 0

        done = False
        for i in range(len(s)):
            if done:
                break
            for j in range(len(s), i, -1):
                sub = s[i:j]
                if j == len(s) and (len(sub) > 1) and (len(set(sub)) == 1):
                    n = len(sub)
                    val = int(n * (n + 1) / 2)
                    count += val
                    done = True
                    break
                isP = isPalindrome(sub)
                count += isP

        return count

        
def isPalindrome(s):
    if len(s) < 2:
        return 1
    if s[0] != s[-1]:
        return 0
    return isPalindrome(s[1:-1])


cases = [
    ("", 0),
    ("hello", 6),
    ("aaab", 7),
    ("baaa", 7),
    ("baaab", 9),
    ("abc", 3),
    ("fdsklf", 6),
    ("a", 1),
    ("aa", 3),
    ("aaa", 6),
    ("aaaa", 10),
    ("aaaaa", 15),
    ("aaaaaa", 21),
    ("aaaaaaa", 28),
    ("aaaaaaaa", 36),
    ("aaaaaaaaa", 45),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 500500),
    ]


if __name__ == '__main__':
    s = Solution()
    for inPut, outPut in cases:
        result = s.countSubstrings(inPut)
        if result == outPut:
            print(True)
        else:
            print(False, inPut, result, outPut)
