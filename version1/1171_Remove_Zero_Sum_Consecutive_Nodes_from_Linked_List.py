"""
Given the head of a linked list,
we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input:
    head = [1,2,-3,3,1]
Output:
    [3,1]
Note:
    The answer [1,2,1] would also be accepted.

Example 2:

Input:
    head = [1,2,3,-3,4]
Output:
    [1,2,4]

Example 3:

Input:
    head = [1,2,3,-3,-2]
Output:
    [1]


Constraints:

    The given linked list will contain between 1 and 1000 nodes.
    Each node in the linked list has -1000 <= node.val <= 1000.
"""
from list_helper import *


class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s, h = 0, ListNode(0)
        h.next = head
        cur = h
        cache = {}
        while cur:
            s += cur.val
            if s in cache:
                hh = cache[s].next
                ss = s
                while hh != cur:
                    ss += hh.val
                    del cache[ss]
                    hh = hh.next
                cache[s].next = cur.next
            else:
                cache[s] = cur
            cur = cur.next
        return h.next


examples = [
    {
        "input": {
            "head": [1, 2, -3, 3, 1],
        },
        "output": [3, 1]
    }, {
        "input": {
            "head": [1, 2, 3, -3, 4],
        },
        "output": [1, 2, 4]
    }, {
        "input": {
            "head": [1, 2, 3, -3, -2],
        },
        "output": [1]
    }, {
        "input": {
            "head": [1, 3, 2, -3, -2, 5, 5, -5, 1],
        },
        "output": [1, 5, 1]
    }, {
        "input": {
            "head": [0, 0],
        },
        "output": []
    }, {
        "input": {
            "head": [2, 2, -2, 1, -1, -1],
        },
        "output": [2, -1]
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        head = generate_list_from_array(example['input']['head'])
        v = func(head)
        end = time.time()
        print_list(v)
        # print v, v == example['output'], end - start