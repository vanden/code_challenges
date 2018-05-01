# https://leetcode.com/problems/bulb-switcher/description/

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Too slow. Failed when hit n=9999
        if n == 0:
            return 0

        bulbs = [False] * n

        for i in range(1, n+1):
            print(i)
            for bulbIdx in range(n):
                if not (bulbIdx + 1) % i:
                    bulbs[bulbIdx] = not bulbs[bulbIdx]
            print(bulbs)

        return len([b for b in bulbs if b])


s = Solution()
s.bulbSwitch(1)
