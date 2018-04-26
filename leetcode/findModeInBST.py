# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counts = self.getCounts(root, defaultdict(int))

        modes = []
        max_count = -1

        for val in counts:
            
            if counts[val] > max_count:
                max_count = counts[val]
                modes = [val,]
            elif counts[val] == max_count:
                modes.append(val)

        return modes
        

    def getCounts(self, root, counts):
        if root is None:
            return counts
        counts[root.val] += 1
        if root.left:
            self.getCounts(root.left, counts)

        if root.right:
            self.getCounts(root.right, counts)

        return counts
