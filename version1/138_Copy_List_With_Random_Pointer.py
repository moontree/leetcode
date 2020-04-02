"""
A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
# Definition for singly-linked list with a random pointer.


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def copy_random_list(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    if head is None:
        return None
    dict = {}
    new_head = RandomListNode(head.label)
    dict[head] = new_head
    c_head = new_head
    cur = head
    while cur.next:
        c_head.next = RandomListNode(cur.next.label)
        dict[cur.next] = c_head.next
        cur = cur.next
        c_head = c_head.next
    c_head = new_head
    cur = head
    while cur:
        if cur.random:
            if dict.get(cur.random) is None:
                tmp = RandomListNode(cur.random.label)
                dict[cur.random] = tmp
                c_head.random = tmp
            else:
                c_head.random = dict.get(cur.random)
        cur = cur.next
        c_head = c_head.next
    return new_head
