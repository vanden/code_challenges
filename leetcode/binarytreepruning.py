# https://leetcode.com/problems/binary-tree-pruning/description/

## I feel like this is probably way too complex


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.containsOnes(root)
        if not root.left is None:
            if not root.left.hasOne:
                root.left = None
            else:
                self.pruneTree(root.left)
        if not root.right is None:
            if not root.right.hasOne:
                root.right = None
            else:
                self.pruneTree(root.right)
        return root

    def containsOnes(self, root):
        root.hasOne = False
        if root.val == 1:
            root.hasOne = True
        if not root.left is None:
            self.containsOnes(root.left)
        if not root.right is None:
            self.containsOnes(root.right)
        root.hasOne = (root.hasOne or
                       ((not root.left is None) and root.left.hasOne) or
                       ((not root.right is None) and root.right.hasOne))
