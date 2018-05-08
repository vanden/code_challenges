#!/usr/bin/env python3
#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/931/
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# First run, 60ms. Same code, second run 44ms beating 97.03 other Py3.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        toExplore = [root]
        levels = []

        while toExplore:
            current = toExplore
            toExplore = []
            level = []
            for node in current:
                level.append(node.val)
                toExplore.extend([n for n in (node.left, node.right) if n])
            levels.append(level)
        return levels

