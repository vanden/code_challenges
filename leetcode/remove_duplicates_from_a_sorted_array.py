# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Yikes!

# Runtime: 10600 ms, faster than 1.00% of Python3 online submissions for
# Remove Duplicates from Sorted Array.

# Memory Usage: 14 MB, less than 0.99% of Python3 online submissions for
# Remove Duplicates from Sorted Array.

class Solution1:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)

        i = 1
        dupeCount = 0
        while i < len(nums):
            if nums[i-1] == nums[i]:
                dupeCount += 1
                # I feel like I should be able to arrange doing just a single copy.
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
            else:
                i += 1
            if dupeCount + i == len(nums):
                break
        return i

################

# No real help.

# Runtime: 10800 ms, faster than 1.00% of Python3 online submissions for
# Remove Duplicates from Sorted Array.

# Memory Usage: 14.1 MB, less than 0.99% of Python3 online submissions for
# Remove Duplicates from Sorted Array.


class Solution2:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)

        i = 1
        dupeCount = 0
        while i < len(nums):
            if nums[i-1] == nums[i]:
                dupeCount += 1
                # I feel like I should be able to arrange doing just a single copy.
                for j in range(i, len(nums)-1):
                    nums[j] = nums[j+1]
            else:
                i += 1
            if dupeCount + i == len(nums):
                break
            if nums[i-1] == nums[-1]:
                # I doubt that this will provide a huge speed-up, but it will
                # clearly help. If there were n duplicates, it will avoid n
                # rounds of shifting the entire tail of nothing but the final
                # number. (I begin to suspect that many of the faster ones are
                # not respecting the O(1) memory constraint. But then I am
                # also apparently consuming a lot of memory in my first try,
                # which doesn't really make sense, either.)
                break
        return i

################

# Gave up and looked at the suggested solution code. I should have listened to
# myself "I feel like I should be able to arrange doing just a single copy."

# Runtime: 60 ms, faster than 85.03% of Python3 online submissions for Remove
# Duplicates from Sorted Array.

# Memory Usage: 14.3 MB, less than 0.99% of Python3 online submissions for
# Remove Duplicates from Sorted Array.


class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        if len(nums) < 2:
            return len(nums)

        i = 0

        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        print(nums, nums[:i+1])
        return i + 1


if __name__ == "__main__":
    s = Solution()
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5])
    s.removeDuplicates([1, 1, 2, 3, 3, 4, 4, 4, 5])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 5, 5, 5])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 8])
    s.removeDuplicates([1, 2, 3, 3, 4, 4, 4, 5, 6, 6, 7, 7, 8])
