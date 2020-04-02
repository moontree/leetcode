"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.
"""


def get_intersection_node(headA, headB):
    """
    :type headA: ListNode
    :type headB: ListNode
    :rtype: ListNode
    """
    if not headA or not headB:
        return None
    p = headA
    while p.next:
        p = p.next
    mark = p
    # make a cycled list
    mark.next = headA
    rst = None
    p1 = headB
    p2 = headB
    while p1 and p2:
        p1 = p1.next
        p2 = p2.next
        if p2:
            p2 = p2.next
        if p1 == p2:
            break
    if p1 and p2 and p1 == p2:
        p1 = headB
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        rst = p1
    # unmake the cycle
    mark.next = None
    return rst
