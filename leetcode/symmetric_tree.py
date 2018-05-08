# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not(root and (root.left or root.right)):
            return True
        if not (root.left and root.right):
            return False
        
        toExplore = [root]

        while any(toExplore):
            current = toExplore
            toExplore = []
            for idx, node in enumerate(current):
                reflect = current[len(current) - idx - 1]
                if node:
                    toExplore.extend([node.left, node.right])
                    if not(reflect and reflect.val == node.val):
                        return False
                else:
                    toExplore.extend([None, None])
                    if reflect:
                        return False
        return True
