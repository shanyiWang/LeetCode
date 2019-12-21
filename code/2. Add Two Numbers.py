'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a code.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    #
    def addTwoNumbers1(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lres = ListNode(-1)
        cur = lres
        cur_l1, cur_l2 = l1, l2
        val_l1, val_l2 = 0, 0
        flag = 0

        while cur_l1 != None or cur_l2 != None or flag == 1:
            if cur_l1 == None:
                val_l1 = 0
            else:
                val_l1 = cur_l1.val
            if cur_l2 == None:
                val_l2 = 0
            else:
                val_l2 = cur_l2.val

            val = val_l1 + val_l2 + flag
            if val >= 10:
                val = val % 10
                flag = 1
            else:
                flag = 0
            node = ListNode(val)
            cur.next = node
            cur = cur.next
            if cur_l1 != None:
                cur_l1 = cur_l1.next
            if cur_l2 != None:
                cur_l2 = cur_l2.next
        return lres.next