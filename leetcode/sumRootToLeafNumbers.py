# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        nums = self.nodeNums(root)
        return sum(int(num) for num in nums)

    def nodeNums(self, root):

        nums = []

        if root.left:
            nums.extend(self.nodeNums(root.left))
        if root.right:
            nums.extend(self.nodeNums(root.right))

        if nums:
            val = str(root.val)
            nums = [val + num for num in nums]
        else:
            nums = [str(root.val),]

        return nums
