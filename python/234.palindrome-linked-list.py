#
# @lc app=leetcode id=234 lang=python
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from pydoc import doc
import copy

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reversed_head = ListNode(head.val)
        head_copy = copy.deepcopy(head)
        reversed_head = None

        while head_copy:
            temp = head_copy.next
            head_copy.next = reversed_head
            reversed_head = head_copy
            head_copy = temp

        ans = True
        while head:
            if head.val != reversed_head.val:
                ans = False
                break
            else:
                head = head.next
                reversed_head = reversed_head.next

        return ans
        
# @lc code=end

