# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Came in as beating 97.77% of Py3 solutions

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        maxes = []

        if not root:
            return maxes

        toExplore = [root]

        while toExplore:
            current = toExplore
            currentMax = float('-inf')
            toExplore = []

            for node in current:
                if node is None:
                    continue
                if node.val > currentMax:
                    currentMax = node.val
                toExplore.extend([n for n in (node.left, node.right) if n])
            maxes.append(currentMax)

        return maxes
