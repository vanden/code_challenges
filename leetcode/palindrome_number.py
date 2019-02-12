# https://leetcode.com/problems/palindrome-number/

# Runtime: 248 ms, faster than 85.12% of Python3 online submissions for
# Palindrome Number.

# Memory Usage: 12.9 MB, less than 0.98% of Python3 online submissions for
# Palindrome Number.

class Solution1:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        return isPalindrome(s)

def isPalindrome(s):
    if len(s) < 2:
        return True

    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    return False

# Runtime: 252 ms, faster than 82.78% of Python3 online submissions for
# Palindrome Number.

# Memory Usage: 12.9 MB, less than 0.98% of Python3 online submissions for
# Palindrome Number.

# So, recursion makes almost no difference to the runtime or memory. I'm
# surpised.

class Solution:
    def isPalindrome(self, x: 'int') -> 'bool':
        s = str(x)
        while True:
            if len(s) < 2:
                return True
            if s[0] != s[-1]:
                return False
            s = s[1:-1]



cases = [
    (10, False),
    (121, True),
    (-121, False),
    (11, True),
    (10000021, False)
]

if __name__ == "__main__":
    s = Solution()
    for i, o in cases:
        result = s.isPalindrome(i)
        if result == o:
            print(True)
        else:
            print(False, result, i, o)
