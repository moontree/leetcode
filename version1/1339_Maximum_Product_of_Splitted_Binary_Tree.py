"""
=========================
Project -> File: leetcode -> 1339_Maximum_Product_of_Splitted_Binary_Tree.py
Author: zhangchao
=========================
Given a binary tree root.
Split the binary tree into two subtrees by removing 1 edge
such that the product of the sums of the subtrees are maximized.

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input:
    root = [1,2,3,4,5,6]
Output:
    110
Explanation:
    Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

Example 2:

Input:
    root = [1,None,2,3,4,None,None,5,6]
Output:
    90
Explanation:
    Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)

Example 3:

Input:
    root = [2,3,9,10,7,8,6,5,4,11,1]
Output:
    1025

Example 4:

Input:
    root = [1,1]
Output:
    1

Constraints:

    Each tree has at most 50000 nodes and at least 2 nodes.
    Each node's value is between [1, 10000].
"""


class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.s = 0
        self.val = 0
        base = 10 ** 9 + 7

        def get_sum(cur):
            if not cur:
                return 0
            if cur:
                l, r = get_sum(cur.left), get_sum(cur.right)
                cur.val = l + r + cur.val
                return cur.val

        def helper(cur):
            if not cur:
                return
            if abs(self.t - cur.val) < abs(self.t - cur.val):
                self.val = cur.val
            # self.res = max(self.res, (self.s - cur.val) * cur.val)
            helper(cur.left)
            helper(cur.right)
        self.s = get_sum(root)
        self.t = self.s * 1.0 / 2
        helper(root)
        return self.val * (self.s - self.val) % base


        
examples = [
    {
        "input": {
            "root": [1, 2, 3, 4, 5, 6],
        },
        "output": 110
    }, {
        "input": {
            "root": [1, None, 2, 3, 4, None, None, 5, 6],
        },
        "output": 90
    }, {
        "input": {
            "root": [2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1],
        },
        "output": 1025
    }, {
        "input": {
            "root": [1, 1],
        },
        "output": 1
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
        print v, v == example['output'], end - start
