# https://leetcode.com/problems/maximum-width-of-binary-tree/description/

class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxWidth = -1
        toExplore = [root]

        while any(toExplore):
            current = toExplore
            toExplore = []
            levelVals = []
            for node in current:
                if node:
                    levelVals.append(node.val)
                    toExplore.extend([node.left, node.right])
                else:
                    if levelVals:
                        # Don't put Nones in front as they aren't spacers
                        levelVals.append(None)
                    if toExplore:
                        # Similar reason; cuts down search space.
                        toExplore.extend([None, None])
            while levelVals and levelVals[-1] is None:
                # Remove non-sapcers
                levelVals.pop()
            while toExplore and toExplore[-1] is None:
                # Cut search space
                toExplore.pop()
            maxWidth = max(maxWidth, len(levelVals))
        return maxWidth
