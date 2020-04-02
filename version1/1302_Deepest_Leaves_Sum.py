"""
=========================
Project -> File: leetcode -> 1302_Deepest_Leaves_Sum.py
Author: zhangchao
=========================
Given a binary tree, return the sum of values of its deepest leaves.

Example 1:

Input:
    root = [1,2,3,4,5,None,6,7,None,None,None,None,8]
Output:
    15


Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The value of nodes is between 1 and 100.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.res = 0

        def helper(cur, d):
            if not cur:
                return
            if self.max_depth < d:
                self.res = cur.val
                self.max_depth = d
            elif self.max_depth == d:
                self.res += cur.val
            else:
                pass
            helper(cur.left, d + 1)
            helper(cur.right, d + 1)

        helper(root, 0)
        return self.res
    

examples = [
    {
        "input": {
            "root": [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8],
        },
        "output": 15
    },
]

import time
#
# if __name__ == '__main__':
#     solution = Solution()
#     for n in dir(solution):
#         if not n.startswith('__'):
#             func = getattr(solution, n)
#     print(func)
#     for example in examples:
#         print '----------'
#         start = time.time()
#         v = func(**example['input'])
#         end = time.time()
#         print v, v == example['output'], end - start
