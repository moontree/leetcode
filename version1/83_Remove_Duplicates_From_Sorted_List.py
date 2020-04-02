"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

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
        "nums": [1, 1, 1, 2, 2, 2, 3],
        "length": 5
    }, {
        "nums": [1, 2, 2, 2, 3],
        "length": 4
    }, {
        "nums": [1, 1, 1, 1, 1, 1],
        "length": 2
    }, {
        "nums": [1, 2, 2, 2, 2, 3, 3, 3, 3],
        "length": 5
    }, {
        "nums": [1, 1, 1, 2, 3],
        "length": 4
    }, {
        "nums": [1, 1],
        "length": 4
    }
]


def delete_duplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    while current:
        processing = current.next
        while processing and processing.val == current.val:
            processing = processing.next
        current.next = processing
        current = current.next
    return head


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
        res = delete_duplicates(t_head)
        print_node(res)
