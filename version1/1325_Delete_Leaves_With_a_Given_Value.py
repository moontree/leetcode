"""
=========================
Project -> File: leetcode -> 1325_Delete_Leaves_With_a_Given_Value.py
Author: zhangchao
=========================
Given a binary tree root and an integer target,
delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target,
if it's parent node becomes a leaf node and has the value target,
it should also be deleted (you need to continue doing that until you can't).



Example 1:

Input:
    root = [1,2,3,2,None,2,4], target = 2
Output:
    [1,None,3,None,4]
Explanation:
    Leaf nodes in green with value (target = 2) are removed (Picture in left).
    After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).

Example 2:

Input:
    root = [1,3,3,3,2], target = 3
Output:
    [1,3,None,None,2]

Example 3:

Input:
    root = [1,2,None,2,None,2], target = 2
Output:
    [1]
Explanation:
    Leaf nodes in green with value (target = 2) are removed at each step.

Example 4:

Input:
    root = [1,1,1], target = 1
Output:
    []

Example 5:

Input:
    root = [1,2,3], target = 1
Output:
    [1,2,3]


Constraints:

    1 <= target <= 1000
    Each tree has at most 3000 nodes.
    Each node's value is between [1, 1000].
"""
from tree_helper import *


class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        # root = generate_tree_from_array(root)

        def helper(cur):
            if cur is None:
                return None
            else:
                cur.left = helper(cur.left)
                cur.right = helper(cur.right)
                if cur.val == target and cur.left is None and cur.right is None:
                    return None
                else:
                    return cur

        res = helper(root)
        return res


examples = [
    {
        "input": {
            "root": [1, 2, 3, 2, None, 2, 4],
            "target": 2
        },
        "target": [1, None, 3, None, 4]
    }, {
        "input": {
            "root": [1, 3, 3, 3, 2],
            "target": 3
        },
        "target": [1, 3, None, None, 2]
    }, {
        "input": {
            "root": [1, 2, None, 2, None, 2],
            "target": 2
        },
        "target": [1]
    }, {
        "input": {
            "root": [1, 1, 1],
            "target": 1
        },
        "target": []
    }, {
        "input": {
            "root": [1, 2, 3],
            "target": 1
        },
        "target": [1, 2, 3]
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
