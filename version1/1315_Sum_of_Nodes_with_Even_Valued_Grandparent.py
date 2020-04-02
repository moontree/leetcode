"""
Given a binary tree,
return the sum of values of nodes with even-valued grandparent.
 (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.


Example 1:

Input:
    root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output:
    18
Explanation:
    The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.


Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.
"""
from tree_helper import *


class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(cur, gp, p):
            if cur:
                if gp is not None and gp % 2 == 0:
                    self.res += cur.val
                helper(cur.left, p, cur.val)
                helper(cur.right, p, cur.val)

        helper(root, None, None)
        return self.res


examples = [
    {
        "input": {
            "root": [6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5],
        },
        "output":18
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
