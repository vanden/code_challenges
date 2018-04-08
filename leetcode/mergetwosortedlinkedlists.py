#!/usr/bin/env python3
#https://leetcode.com/problems/merge-two-sorted-lists/description/

# Given API for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not (l1 and l2):
            return l1 or l2

        newList = ListNode(-42)
        prior = newList
        
        while l1 and l2:
            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
                
            prior.next = ListNode(val)                
            prior = prior.next

        prior.next = l1 or l2

        return newList.next
