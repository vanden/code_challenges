# https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        revdigitstring = ''.join(reversed(str(x)))
        if revdigitstring[-1] == '-':
            revdigitstring = '-' + revdigitstring[:-1]
        num = int(revdigitstring)
        if num > (2**31) or num < -(2**31):
            num = 0
        return num
