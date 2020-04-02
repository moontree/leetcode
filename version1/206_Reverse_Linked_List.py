"""
Reverse a singly linked list.
"""
from list_helper import *


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur = None
    while head:
        next_node = head.next
        head.next = cur
        cur = head
        head = next_node
    return cur


examples = [
    {
        "nums": [1, 2, 3],
    }, {
        "nums": []
    }
]


for example in examples:
    l = generate_list_from_array(example["nums"])
    print_list(l)
    print_list(reverse_list(l))
