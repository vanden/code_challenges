# https://leetcode.com/problems/remove-element/

# Wat

# Runtime: 36 ms, faster than 99.96% of Python3 online submissions for Remove
# Element.

# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for
# Remove Element.


class Solution:
    def removeElement(self, nums: 'List[int]', val: 'int') -> 'int':

        shifts = 0
        done = False
        for i in range(len(nums)):
            while nums[i] == val:
                shifts += 1
                for j in range(i, len(nums)-1):
                    # But, I'd like something smarter. However, the results
                    # above suggest that isn't to be found.
                    nums[j] = nums[j+1]
                if shifts + i >= len(nums):
                    done = True
                    break
            if done:
                break
        return len(nums) - shifts



if __name__ == "__main__":

    cases = [
        ([3,2,2,3], 3),
        ([0,1,2,2,3,0,4,2], 2),
        ]

    s = Solution()

    for array, val in cases:
        s.removeElement(array, val)

