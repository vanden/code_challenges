# https://leetcode.com/problems/masking-personal-information/

# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for
# Masking Personal Information.

# Memory Usage: 6.4 MB, less than 85.19% of Python3 online submissions for
# Masking Personal Information.

class Solution:
    def maskPII(self, S: 'str') -> 'str':
        if "@" in S:
            return self.maskEmail(S)
        return self.maskPhoneNumber(S)

    def maskEmail(self, S):
        S = S.lower()
        name, domain = S.split('@')
        name = name[0] + '*****' + name[-1]
        return '@'.join([name, domain])

    def maskPhoneNumber(self, S):
        digits = [c for c in S if c.isdigit()]
        result = []
        if len(digits) > 10:
            result.append('+%s-' %('*' * (len(digits) - 10)))
        result.append('***-***-')
        result.extend(digits[-4:])
        return ''.join(result)


cases = [
    ("LeetCode@LeetCode.com", "l*****e@leetcode.com"),
    ("AB@qq.com", "a*****b@qq.com"),
    ("1(234)567-890", "***-***-7890"),
    ("86-(10)12345678", "+**-***-***-5678")
]


if __name__ == "__main__":

    s = Solution()

    for inPut, outPut in cases:
        if outPut == s.maskPII(inPut):
            print(True)
        else:
            print(inPut, s.maskPII(inPut), outPut)
