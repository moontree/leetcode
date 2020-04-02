"""
=========================
Project -> File: leetcode -> 1305_All_Elements_in_Two_Binary_Search_Trees.py
Author: zhangchao
=========================
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:

Input:
    root1 = [2,1,4], root2 = [1,0,3]
Output:
    [0,1,1,2,3,4]

Example 2:

Input:
    root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output:
    [-10,0,0,1,2,5,7,10]

Example 3:

Input:
    root1 = [], root2 = [5,1,7,0,2]
Output:
    [0,1,2,5,7]

Example 4:

Input:
    root1 = [0,-10,10], root2 = []
Output:
    [-10,0,10]

Example 5:

Input:
    root1 = [1,None,8], root2 = [8,1]
Output:
    [1,1,8,8]


Constraints:

    Each tree has at most 5000 nodes.
    Each node's value is between [-10^5, 10^5].
"""

from tree_helper import *


class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        root1, root2 = generate_tree_from_array(root1), generate_tree_from_array(root2)

        def helper(root):
            res = []
            q, cur = [], root
            while q or cur:
                while cur:
                    q.append(cur)
                    cur = cur.left
                # print [v.val for v in q], cur.val if cur else -1
                cur = q.pop()
                res.append(cur.val)
                cur = cur.right
            return res

        res = []
        q1, q2 = helper(root1), helper(root2)
        i, j = 0, 0
        while i < len(q1) and j < len(q2):
            if q1[i] < q2[j]:
                res.append(q1[i])
                i += 1
            else:
                res.append(q2[j])
                j += 1
        res += q1[i:] + q2[j:]
        return res
        

examples = [
    {
        "input": {
            "root1": [2, 1, 4],
            "root2": [1, 0, 3]
        },
        "output": [0, 1, 1, 2, 3, 4]
    }, {
        "input": {
            "root1": [0, -10, 10],
            "root2": [5, 1, 7, 0, 2]
        },
        "output": [-10, 0, 0, 1, 2, 5, 7, 10]
    }, {
        "input": {
            "root1": [],
            "root2": [5, 1, 7, 0, 2]
        },
        "output": [0, 1, 2, 5, 7]
    }, {
        "input": {
            "root1": [0, -10, 10],
            "root2": []
        },
        "output": [-10, 0, 10]
    }, {
        "input": {
            "root1": [1, None, 8],
            "root2": [8, 1]
        },
        "output": [1, 1, 8, 8]
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
