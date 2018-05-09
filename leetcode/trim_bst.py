# https://leetcode.com/problems/trim-a-binary-search-tree/description/

# Beats 97.66% of Py3 solutions at 64ms. But, also seems too complex.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root

        # Find correct root
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
                if root is None:
                    return None
            if root.val > R:
                root = root.left
                if root is None:
                    return None

        # Find correct left and right children
        while not(root.left is None) and root.left.val < L:
            root.left = root.left.right
        while not(root.right is None) and root.right.val > R:
            root.right = root.right.left

        # Recurse
        root.right = self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)

        return root
