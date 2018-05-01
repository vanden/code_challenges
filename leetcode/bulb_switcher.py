# https://leetcode.com/problems/bulb-switcher/description/

from collections import defaultdict

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Not sure this is an improvement, but still times out on same case.
        if n == 0:
            return 0

        toggle_counts = defaultdict(int)

        for i in range(1, n+1):
            for bulbIdx in range(n):
                if not (bulbIdx + 1) % i:
                    toggle_counts[bulbIdx] += 1

        return len([c for c in toggle_counts.values() if c%2])


s = Solution()
s.bulbSwitch(1)
