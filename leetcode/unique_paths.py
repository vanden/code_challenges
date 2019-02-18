# https://leetcode.com/problems/unique-paths/

# Runtime: 36 ms, faster than 79.20% of Python3 online submissions for Unique Paths.

# Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Unique Paths.

class Solution:
    def uniquePaths(self, m: 'int', n: 'int') -> 'int':
        return int((factorial(n-1+m-1))/(factorial(n-1)*factorial(m-1)))

def factorial(n):
        result = 1
        for i in range(1,n+1):
            result *= i
        return result
