"""
Given a (singly) linked list with head node root,
write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible:
no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list,
and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]

Example 1:
Input:
    root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
    The input and each element of the output are ListNodes, not arrays.
    For example,
    the input root has root.val = 1,
     root.next.val = 2, \root.next.next.val = 3,
     and root.next.next.next = null.
    The first element output[0] has output[0].val = 1, output[0].next = null.
    The last element output[4] is null, but it's string representation as a ListNode is [].

Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(root):
    res = []
    h = root
    while h:
        res.append(h.val)
        h = h.next
    print res


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        c = 0
        h = root
        while h:
            c += 1
            h = h.next
        res = []
        v = c // k
        r = c % k
        # print(c, v, r)
        h, idx = root, 0
        while idx < k:
            cur = h
            if idx < r:
                for _ in range(1, v + 1):
                    if cur:
                        cur = cur.next
            else:
                for _ in range(1, v):
                    if cur:
                        cur = cur.next
            if cur:
                new_head = cur.next
                cur.next = None
                res.append(h)
                h = new_head
            else:
                res.append(h)
                h = None
            idx += 1
        # print ''
        # for r in res:
        #     print_list(r)
        return res


examples = [
    {
        "input": {
            "nums": [1, 2, 3],
            "k": 5
        },
        "output": [[1], [2], [3], [], []]
    },{
        "input": {
            "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            "k": 3
        },
        "output": [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        root = ListNode(0)
        cur = root
        for v in example['input']['nums']:
            n = ListNode(v)
            cur.next = n
            cur = n
        print_list(root.next)
        inputs = {
            "root": root.next,
            "k": example['input']['k']
        }
        func(**inputs)
        # print func(**inputs) == example['output']