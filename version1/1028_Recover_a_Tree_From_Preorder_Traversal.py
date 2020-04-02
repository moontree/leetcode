"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal,
we output D dashes (where D is the depth of this node),
then we output the value of this node.
(If the depth of a node is D, the depth of its immediate child is D+1.
The depth of the root node is 0.)

If a node has only one child,
that child is guaranteed to be the left child.

Given the output S of this traversal,
recover the tree and return its root.



Example 1:

Input:
    "1-2--3--4-5--6--7"
Output:
    [1,2,5,3,4,6,7]


Example 2:

Input:
    "1-2--3---4-5--6---7"
Output:
    [1,2,5,3,null,6,null,4,null,7]

Example 3:

Input:
    "1-401--349---90--88"
Output:
    [1,401,null,349,88,90]

Note:

    The number of nodes in the original tree is between 1 and 1000.
    Each node will have a value between 1 and 10^9.
"""

from tree_helper import *


class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        q = [[0, -1]]
        flag, tmp = 'd', ''
        for c in S:
            if c == '-':
                if flag == 'd':
                    q[-1][1] = int(tmp)
                    tmp = '-'
                    flag = 'h'
                else:
                    tmp += c
            else:
                if flag == 'd':
                    tmp += c
                else:
                    q.append([len(tmp), -1])
                    flag = 'd'
                    tmp = c
        q[-1][1] = int(tmp)
        # print q

        def helper(l, r, h):
            if l == r:
                return TreeNode(q[l][1])
            if l > r:
                return None
            else:
                n = TreeNode(q[l][1])
                mid = r + 1
                for i in range(l + 2, r + 1):
                    if q[i][0] == h + 1:
                        mid = i
                        break
                n.left = helper(l + 1, mid - 1, h + 1)
                n.right = helper(mid, r, h + 1)
                return n

        r = helper(0, len(q) - 1, 0)
        print_tree(r)
        return r
    

examples = [
    {
        "input": {
            "S": "1-2--3--4-5--6--7",
        },
        "output": [1, 2, 5, 3, 4, 6, 7]
    }, {
        "input": {
            "S": "1-2--3---4-5--6---7",
        },
        "output": [1, 2, 5, 3, None, 6, None, 4, None, 7]
    }, {
        "input": {
            "S": "1-401--349---90--88",
        },
        "output": [1, 401, None, 349, 88, 90]
    }
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
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
