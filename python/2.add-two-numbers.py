#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        n2 = 0
        expo = 0
        while l1:
            n1 += l1.val * int(pow(10, expo))
            expo += 1
            l1 = l1.next
        expo = 0
        while l2:
            n2 += l2.val * int(pow(10, expo))
            expo += 1
            l2 = l2.next
        n_sum = n1 + n2
        ans = ListNode()
        temp = ans
        while n_sum != 0:
            if n_sum != n1 + n2:
                temp.next = ListNode(n_sum % 10, None)
                temp = temp.next
            else:
                ans.val = n_sum % 10
            n_sum //= 10

        return ans


# @lc code=end

