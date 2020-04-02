"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

Related Topics

Similar Questions
Add Two Numbers

"""
from list_helper import *


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    c = 0
    header = None
    while s1 and s2:
        v = c + s1.pop() + s2.pop()
        c, v = v / 10, v % 10
        cur = ListNode(v)
        cur.next = header
        header = cur
    while s1:
        v = c + s1.pop()
        c, v = v / 10, v % 10
        cur = ListNode(v)
        cur.next = header
        header = cur
    while s2:
        v = c + s2.pop()
        c, v = v / 10, v % 10
        cur = ListNode(v)
        cur.next = header
        header = cur
    if c:
        cur = ListNode(c)
        cur.next = header
        header = cur
    return header