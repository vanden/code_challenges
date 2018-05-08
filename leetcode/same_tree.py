# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p, q):
        if not (p or q):
            return True
        if (p and q) and (p.val == q.val):
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        return False
