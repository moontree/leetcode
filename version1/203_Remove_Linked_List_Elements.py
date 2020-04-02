"""
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
"""
from list_helper import *


def remove_elements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    nh = ListNode(None)
    nh.next = head
    cur = nh
    while cur:
        if cur.next and cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return nh.next


examples = [
    {
        "nums": [1, 2, 6, 3, 4, 5, 6],
        "val": 6
    }, {
        "nums": [6, 6, 6],
        "val": 6
    }
]


for example in examples:
    h = generate_list_from_array(example["nums"])
    print_list(h)
    print_list(remove_elements(h, example["val"]))
