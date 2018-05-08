# https://leetcode.com/problems/find-bottom-left-tree-value/description/

# Given a binary tree, find the leftmost value in the last row of the tree.

# First thought is to do a level order traversal and note the first element on
# each level, returning the last see first element when out of levels.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        toExplore = [root]
        while toExplore:
            leftmost = toExplore[0]
            current = toExplore
            toExplore = []
            for node in current:
                if node.left:
                    toExplore.append(node.left)
                if node.right:
                    toExplore.append(node.right)
        return leftmost.val
