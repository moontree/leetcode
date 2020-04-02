"""
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
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
        "nums": [1, 4, 3, 2, 5, 2],
        "x": 3,
        "ans": [1, 2, 2, 4, 3, 5]
    }
]


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    h = head
    left = ListNode(-1)
    left_head = left
    right = ListNode(-1)
    right_head = right
    while h:
        if h.val < x:
            left.next = h
            h = h.next
            left = left.next
            left.next = None
        else:
            right.next = h
            h = h.next
            right = right.next
            right.next = None
    left.next = right_head.next
    return left_head.next


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
        res = partition(t_head, example["x"])
        print_node(res)
