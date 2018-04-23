# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = self.inOrderTraversal(root)
        minDiff = float("inf")
        for idx, node in enumerate(nodes[:-1]):
            if nodes[idx+1].val - node.val < minDiff:
                minDiff = nodes[idx+1].val - node.val
        return minDiff

    def inOrderTraversal(self, root):
        if root is None:
            return []
        nodes = self.inOrderTraversal(root.left)
        nodes.append(root)
        nodes.extend(self.inOrderTraversal(root.right))
        return nodes
