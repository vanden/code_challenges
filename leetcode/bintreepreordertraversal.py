#!/usr/bin/env python3
# https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        if root.left:
            result.extend(self.preorderTraversal(root.left))
        if root.right:
            result.extend(self.preorderTraversal(root.right))
        return result
            
