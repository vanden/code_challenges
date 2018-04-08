#!/usr/bin/env python3
#https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = self.postorderTraversal(root.left)
        result.extend(self.postorderTraversal(root.right))
        result.append(root.val)

        return result

                      
