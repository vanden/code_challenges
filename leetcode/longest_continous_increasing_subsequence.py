# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/

# Runtime: 44 ms, faster than 84.62% of Python3 online submissions for Longest
# Continuous Increasing Subsequence.

# Memory Usage: 7.6 MB, less than 89.42% of Python3 online submissions for
# Longest Continuous Increasing Subsequence.


class Solution1:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        longest = 0
        current = 0
        last = None
        for _, num in enumerate(nums):
            if not current:
                current = 1
                last = num
                longest = 1
                continue

            if num > last:
                current += 1
                longest = max(longest, current)
            else:
                longest = max(longest, current)
                current = 1
            last = num
        return longest


# Runtime: 40 ms, faster than 99.41% of Python3 online submissions for Longest
# Continuous Increasing Subsequence.

# Memory Usage: 7.6 MB, less than 93.91% of Python3 online submissions for
# Longest Continuous Increasing Subsequence.

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        longest = 1
        current = 1
        last = nums[0]
        for _, num in enumerate(nums[1:]):
            if num > last:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
            last = num
        return longest



cases = [
    ([1,3,5,7], 4),
    ([1,3,5,4,2,3,4,5], 4),
    ]

if __name__ == "__main__":
    s = Solution()
    for inPut, outPut in cases:
        print(s.findLengthOfLCIS(inPut) == outPut)
