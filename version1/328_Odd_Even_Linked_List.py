"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
 Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""
from list_helper import *


def odd_even_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    odd_head, even_head = head, head.next
    odd, even = odd_head, even_head
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return odd_head


examples = [
    {
        "nums": [1, 2, 3, 4, 5]
    }
]


for example in examples:
    lh = generate_list_from_array(example["nums"])
    print_list(odd_even_list(lh))
