"""
Given a singly linked list L: 0, 1, 2, ..., n
reorder it to: 0, n, 1, n-1, 2, n - 2, ...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
from list_helper import *


def reorder_list(head):
    """
    :type head: ListNode
    :rtype: void Do not return anything, modify head in-place instead.
    """
    if head is None:
        return head
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    pre, slow.next, slow = None, None, slow.next
    pre, last_head = None, None
    while slow:
        to_do = slow.next
        cur = slow
        cur.next = pre
        pre = cur
        last_head = cur
        slow = to_do
    s, t = head, last_head
    while s and t:
        t.next, s.next, s, t = s.next, t, s.next, t.next
        # tn = t.next
        # t.next = s.next
        # s.next = t
        # s = s.next.next
        # t = tn


examples = [
    {
        "nums": [1, 2, 3, 4, 5, 6, 7, 8]
    }, {
        "nums": [1, 2, 3, 4, 5]
    }, {
        "nums": [1]
    }
]


for example in examples:
    list_head = generate_list_from_array(example["nums"])
    print_list(list_head)
    reorder_list(list_head)
    print_list(list_head)
