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
        if not (p and q) or (p.val != q.val):
            return False
        if not (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)):
            return False
        return True
