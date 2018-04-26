# https://leetcode.com/problems/student-attendance-record-i/description/

class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        abCount = 0
        continousLateCount = 0

        for c in s:
            if c == 'A':
                abCount += 1
                if abCount > 1:
                    return False
                
            if c == 'L':
                continousLateCount += 1
                if continousLateCount > 2:
                    return False
            else:
                continousLateCount = 0

        return True
