# https://leetcode.com/problems/reverse-vowels-of-a-string/

# Runtime: 68 ms, faster than 75.70% of Python3 online submissions for Reverse
# Vowels of a String.

# Memory Usage: 15.1 MB, less than 1.72% of Python3 online submissions for
# Reverse Vowels of a String.


class Solution:
    def reverseVowels(self, s: 'str') -> 'str':

        vowels = []
        indicies = []
        result = list(s)
        for i, c in enumerate(s):
            if c.lower() in 'aeiou':
                vowels.append(c)
                indicies.append(i)

        for i in indicies:
            vowel = vowels.pop()
            result[i] = vowel

        return ''.join(result)


cases = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        result = s.reverseVowels(inPut)
        if result != outPut:
            print(inPut, result, outPut)
