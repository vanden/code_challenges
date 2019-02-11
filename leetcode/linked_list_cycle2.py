# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Runtime: 44 ms, faster than 99.67% of Python online submissions for Linked
# List Cycle II.

# Memory Usage: 18.4 MB, less than 18.83% of Python online submissions for
# Linked List Cycle II.

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        seen = set([head])
        tortise = head
        hare = head
        while hare and hare.next:
            hare = hare.next
            if hare is None:
                return None
            tortise = tortise.next
            if tortise in seen:
                return tortise
            seen.add(tortise)
            hare = hare.next
        return None
