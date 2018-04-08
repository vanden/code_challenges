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
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            newList = ListNode(l1.val)
            l1 = l1.next
        else:
            newList = ListNode(l2.val)
            l2 = l2.next
        prior = newList
        
        while l1 and l2:
            if l1.val < l2.val:
                prior.next = ListNode(l1.val)
                l1 = l1.next
            else:
                prior.next = ListNode(l2.val)
                l2 = l2.next
                
            prior = prior.next

        if l1:
            prior.next = l1
        else:
            prior.next = l2

        return newList
