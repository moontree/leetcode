"""
=========================
Project -> File: leetcode -> 1382_Balance_a_Binary_Search_Tree.py
Author: zhangchao
=========================
Given a binary search tree,
return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

Example 1:
Input:
    root = [1,null,2,null,3,null,4,null,null]
Output:
    [2,1,3,null,null,null,4]
Explanation:
    This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.

Constraints:

    The number of nodes in the tree is between 1 and 10^4.
    The tree nodes will have distinct values between 1 and 10^5.
"""
from tree_helper import *


class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def helper(cur):
            if cur is None:
                return []
            return helper(cur.left) + [cur.val] + helper(cur.right)

        nums = helper(root)

        def generate(l, r):
            if l > r:
                return None
            mid = (l + r) / 2
            node = TreeNode(nums[mid])
            node.left = generate(l, mid - 1)
            node.right = generate(mid + 1, r)
            return node

        return generate(0, len(nums) - 1)


examples = [
    {
        "input": {
            "root": [1, None, 2, None, 3, None, 4, None, None],
        },
        "output": [2, 1, 3, None, None, None, 4],
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
