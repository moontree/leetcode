"""
Given a singly linked list, determine if it is a palindrome.
"""
from list_helper import *


def is_palindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    if fast == slow:
        return True
    right_tail = None
    right_head = None
    while slow:
        right_head = slow
        slow = slow.next
        right_head.next = right_tail
        right_tail = right_head
    cur = right_head
    while cur:
        if cur.val != head.val:
            return False
        else:
            cur = cur.next
            head = head.next
    return True


examples = [
    {
        "nums": [1, 2, 3, 2, 1],
        "res": True
    }, {
        "nums": [1, 2, 2, 1],
        "res": True
    }, {
        "nums": [1, 2],
        "res": False
    }, {
        "nums": [1],
        "res": True
    }
]


for example in examples:
    lh = generate_list_from_array(example["nums"])
    print is_palindrome(lh)
