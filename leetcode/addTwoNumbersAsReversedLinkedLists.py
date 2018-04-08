#!/usr/bin/env python3
# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(None)
        prior = result
        while l1 or l2 or carry:
            if l1:
                d1 = l1.val
                l1 = l1.next
            else: 
                d1 = 0
            if l2:
                d2 = l2.val
                l2 = l2.next                
            else:
                d2 = 0
            digitSum = d1 + d2 + carry
            prior.next = ListNode(digitSum % 10)
            prior = prior.next
            carry = digitSum // 10
            
        return result.next
