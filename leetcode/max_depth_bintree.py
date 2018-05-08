# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        toExplore = [root]
        depth = 0
        
        while toExplore:
            depth += 1
            current = toExplore
            toExplore = []
            for node in current:
                toExplore.extend([n for n in (node.left, node.right) if n])

        return depth
