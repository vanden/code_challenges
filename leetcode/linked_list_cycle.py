# https://leetcode.com/problems/linked-list-cycle/submissions/

# Runtime: 44 ms, faster than 94.95% of Python online submissions for Linked
# List Cycle.

# Memory Usage: 16.2 MB, less than 82.22% of Python online submissions for
# Linked List Cycle.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        tortise = head
        hare = head
        while True:
            hare = hare.next
            tortise = tortise.next
            if hare is None:
                return False
            hare = hare.next
            if hare is None:
                return False
            if hare is tortise:
                return True
