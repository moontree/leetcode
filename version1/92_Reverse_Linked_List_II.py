"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1, 2, 3, 4, 5, m = 2 and n = 4,

return 1, 4, 3, 2, 5

Note:
Given m, n satisfy the following condition:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_node(node):
    while node and node.next:
        print node.val, '->',
        node = node.next
    if node:
        print node.val
    else:
        print node


examples = [
    {
        "nums": [1, 2, 3, 4, 5],
        "m": 1,
        "n": 5
    }
]


def reverse_between(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    head_mark = ListNode(-1)
    head_mark.next = head
    tail = head_mark
    current = head
    index = 1
    while index < m:
        tail = tail.next
        current = current.next
        index += 1
    tail.next = None
    partial_tail = current
    partial_head = ListNode(-1)
    while index < n + 1:
        node = current
        current = current.next
        node.next = partial_head
        partial_head = node
        index += 1
    tail.next = partial_head
    partial_tail.next = current
    return head_mark.next


if __name__ == "__main__":
    for example in examples:
        vals = example["nums"]
        t_head = ListNode(vals[0])
        t = t_head
        for i in range(1, len(vals)):
            tmp = ListNode(vals[i])
            t.next = tmp
            t = t.next
        print "------"
        print_node(t_head)
        res = reverse_between(t_head, example["m"], example["n"])
        print_node(res)
