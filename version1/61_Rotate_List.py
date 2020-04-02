"""
Given a list, rotate the list to the right by k places, where k is non-negative.


Example:

Given 1->2->3->4->5->NULL and k = 2,

return 4->5->1->2->3->NULL.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_node(node):
    while node.next:
        print node.val, '->',
        node = node.next
    print node.val


def rotate_right(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if head is None or k == 0:
        return head
    h = head
    tail = head
    count = 1
    while tail.next and count < k:
        tail = tail.next
        count += 1
    tail = h
    if count < k:
        k = k % count
    for j in range(k):
        tail = tail.next
        if tail is None:
            tail = h
    if tail == h:
        return h
    while tail and tail.next:
        h = h.next
        tail = tail.next
    new_head = h.next
    tail.next = head
    h.next = None
    return new_head


examples = [
    {
        "list": [1, 2, 3, 4, 5],
        "k": 2
    }, {
        "list": [1, 2, 3],
        "k": 100
    }, {
        "list": [3],
        "k": 1
    }
]


if __name__ == "__main__":
    for example in examples:
        vals = example["list"]
        t_head = ListNode(vals[0])
        t = t_head
        for i in range(1, len(vals)):
            tmp = ListNode(vals[i])
            t.next = tmp
            t = t.next
        print_node(t_head)
        res = rotate_right(t_head, example['k'])
        print_node(res)
