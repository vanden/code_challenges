# https://leetcode.com/problems/linked-list-cycle/submissions/

# Runtime: 40 ms, faster than 100.00% of Python online submissions for Linked
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
        while hare and hare.next:
            hare = hare.next
            if hare is None:
                return False
            tortise = tortise.next
            hare = hare.next
            if hare is tortise:
                return True
        return False
