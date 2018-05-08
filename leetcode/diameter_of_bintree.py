# https://leetcode.com/problems/diameter-of-binary-tree/description/
class Solution:

    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        throughRoot = (self.maxDepth(root.left) + self.maxDepth(root.right))
        leftDiameter = self.diameterOfBinaryTree(root.left)
        rightDiameter = self.diameterOfBinaryTree(root.right)

        return max(throughRoot, leftDiameter, rightDiameter)

    def maxDepth(self, root):
        # Recycled from solution to
        # https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
        if not root:
            return 0
        toExplore = [root]
        depth = 0

        while toExplore:
            depth += 1
            current = toExplore
            toExplore = []
            for node in current:
                toExplore.extend([n for n in (node.left, node.right) if n])

        return depth
