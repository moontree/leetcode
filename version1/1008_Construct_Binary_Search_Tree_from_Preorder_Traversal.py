"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input:
    [8,5,1,7,10,12]
Output:
    [8,5,10,1,7,null,12]

Note:

    1 <= preorder.length <= 100
    The values of preorder are distinct.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_helper import *
import bisect


class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        def helper(l, r):
            print(l, r)
            if l > r:
                return None
            if l == r:
                return TreeNode(preorder[l])
            val = preorder[l]
            root = TreeNode(val)
            mid = l + 1
            while mid <= r and preorder[mid] < val:
                mid += 1
            root.left = helper(l + 1, mid - 1)
            root.right = helper(mid, r)
            return root

        return helper(0, len(preorder) - 1)


examples = [
    {
        "input": {
            "preorder": [8, 5, 1, 7, 10, 12],
        },
        "output": 20
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
        v = func(**example['input'])
        end = time.time()
        print_tree(v)
        print v, v == example['output'], end - start
