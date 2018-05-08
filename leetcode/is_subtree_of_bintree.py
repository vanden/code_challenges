# https://leetcode.com/problems/subtree-of-another-tree/description/

# Problem spec doesn't say if all node values are unique. I submitted a
# version that assumed they were and failed, accordingly.

# This beats 85.55% of the other Py3 solutions on leetcode with a runtime of
# 200ms. There is at least one in the 80ms range.

class Solution:

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        toExplore = [s]

        while toExplore:
            current = toExplore
            toExplore = []
            for node in current:
                if node.val == t.val:
                    if self.isSameTree(node, t):
                        return True
                toExplore.extend([n for n in (node.left, node.right) if n])
        return False
    
    # Recycled from answer to https://leetcode.com/problems/same-tree/description/
    def isSameTree(self, p, q):
        if not (p or q):
            return True
        if (p and q) and (p.val == q.val):
            return (self.isSameTree(p.right, q.right) and
                    self.isSameTree(p.left, q.left))
        return False
