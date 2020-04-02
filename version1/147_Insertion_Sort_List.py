"""
Sort a linked list using insertion sort.
"""
from list_helper import *


def insertion_sort_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return head
    new_head = ListNode(float('-inf'))
    cur = head
    tail = new_head
    while cur:
        pos = new_head
        pre = new_head
        if cur.val > tail.val:
            tail.next = ListNode(cur.val)
            tail = tail.next
        else:
            while pos and pos.val < cur.val:
                pre, pos = pos, pos.next
            pre.next = ListNode(cur.val)
            pre.next.next = pos
        cur = cur.next
    return new_head.next


examples = [
    {
        "vals": [5, 4, 3, 2, 1]
    }, {
        "vals": [1, 1]
    }
]


for example in examples:
    print '------------'
    lhead = generate_list_from_array(example["vals"])
    print_list(lhead)
    print_list(insertion_sort_list(lhead))
