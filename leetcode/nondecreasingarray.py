# https://leetcode.com/problems/non-decreasing-array/description/

## Broken

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        badCount = 0

        for idx, item in enumerate(nums[:-1]):
            if item > nums[idx+1]:
                badCount += 1
                print(item, nums[idx+1], idx, f"Nums: {nums}", badCount)

                if badCount > 1:
                    return False

                
                if not self.checkPossibility(nums[idx:idx+1]+nums[idx+2:]):
                    return False

        return True


s = Solution()

#print(s.checkPossibility([4,2,3]))

print(s.checkPossibility([3,4,2,3]))
