# https://leetcode.com/problems/partition-labels/description/

# A string S of lowercase letters is given. We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.


# First version:

# Runtime: 408 ms, faster than 1.97% of Python3 online submissions for
# Partition Labels.

# Memory Usage: 6.4 MB, less than 80.75% of Python3 online submissions for
# Partition Labels.

# So, slow, but relatively little memory used. Obviously, trade space for time
# and memoize rindex results

class Solution1:

    def partitionLabels(self, string):
        chunkLengths = []
        i = 0
        lastIndex = -1
        while i < len(string):
            endIdx = string.rindex(string[i])
            j = max(string.rindex(c) for c in string[lastIndex+1:endIdx+1])
            if i == j:
                chunkLengths.append(i-lastIndex)
                lastIndex = i
                i += 1
            else:
                i += 1
        return chunkLengths


class Solution:

    def partitionLabels(self, string):
        chunkLengths = []
        i = 0
        lastIndex = -1
        memo = {}

        def getRIndex(c):
            if not c in memo:
                memo[c] = string.rindex(c)
            return memo[c]


        while i < len(string):
            endIdx = string.rindex(string[i])
            j = max(getRIndex(c) for c in string[lastIndex+1:endIdx+1])
            if i == j:
                chunkLengths.append(i-lastIndex)
                lastIndex = i
                i += 1
            else:
                i += 1
        return chunkLengths



s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("avbabcbacadedehijhklvij"))
print(s.partitionLabels("avbabvij"))
