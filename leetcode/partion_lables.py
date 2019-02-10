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

# Runtime: 344 ms, faster than 2.23% of Python3 online submissions for
# Partition Labels.

# Memory Usage: 6.4 MB, less than 94.84% of Python3 online submissions for
# Partition Labels.

# Barely made a difference

class Solution2:

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

# Runtime: 48 ms, faster than 76.80% of Python3 online submissions for
# Partition Labels.

#Memory Usage: 6.4 MB, less than 99.53% of Python3 online submissions for
#Partition Labels.

# A trivial change (setting i = j rather than i += 1 in the else clause) made
# a huge difference.

class Solution3:

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
                i = j
        return chunkLengths

# Runtime: 44 ms, faster than 94.10% of Python3 online submissions for
# Partition Labels.

# Memory Usage: 6.5 MB, less than 67.61% of Python3 online submissions for
# Partition Labels.

# I'm surprised the dict comp in place of a function call didn't help the
# speed, more.

class Solution4:

    def partitionLabels(self, string):
        chunkLengths = []
        i = 0
        lastIndex = -1
        memo = {c: i for i, c in enumerate(string)}

        while i < len(string):
            endIdx = string.rindex(string[i])
            j = max(memo[c] for c in string[lastIndex+1:endIdx+1])
            if i == j:
                chunkLengths.append(i-lastIndex)
                lastIndex = i
                i += 1
            else:
                i = j
        return chunkLengths


# Runtime: 44 ms, faster than 94.10% of Python3 online submissions for
# Partition Labels.

# Memory Usage: 6.5 MB, less than 58.22% of Python3 online submissions for
# Partition Labels.

# Very surprised that removing the str.rindex call in the while loop in favour
# of the memoized data didn't help at all.

class Solution:

    def partitionLabels(self, string):
        chunkLengths = []
        i = 0
        lastIndex = -1
        memo = {c: i for i, c in enumerate(string)}

        while i < len(string):
            endIdx = memo[string[i]]
            j = max(memo[c] for c in string[lastIndex+1:endIdx+1])
            if i == j:
                chunkLengths.append(i-lastIndex)
                lastIndex = i
                i += 1
            else:
                i = j
        return chunkLengths


s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
print(s.partitionLabels("avbabcbacadedehijhklvij"))
print(s.partitionLabels("avbabvij"))
print(s.partitionLabels("eaaaabaaec"))
