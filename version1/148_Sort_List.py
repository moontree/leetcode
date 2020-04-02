"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
from list_helper import *


def sort_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    return split(head)


def split(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    partial1 = head
    partial2 = slow.next
    slow.next = None
    left = split(partial1)
    right = split(partial2)
    tmp = merge(left, right)
    return tmp


def merge(list1, list2):
    new_head = ListNode(-1)
    h = new_head
    while list1 and list2:
        if list1.val < list2.val:
            h.next = list1
            list1 = list1.next
        else:
            h.next = list2
            list2 = list2.next
        h = h.next
    if list1:
        h.next = list1
    else:
        h.next = list2
    return new_head.next


examples = [
    {
        "nums": [5, 4, 3, 2, 1],
    }, {
        "nums": [1],
    }, {
        "nums": [5, 1],
    }
]


for example in examples:
    hd = generate_list_from_array(example["nums"])
    print_list(hd)
    print_list(sort_list(hd))
