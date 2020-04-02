"""
Given a binary tree with N nodes,
each node has a different value from {1, ..., N}.

A node in this binary tree can be flipped by swapping the left child and the right child of that node.

Consider the sequence of N values reported by a preorder traversal starting from the root.
Call such a sequence of N values the voyage of the tree.

(Recall that a preorder traversal of a node means we report the current node's value,
then preorder-traverse the left child, then preorder-traverse the right child.)

Our goal is to flip the least number of nodes in the tree so that the voyage of the tree matches the voyage we are given.

If we can do so, then return a list of the values of all nodes flipped.
You may return the answer in any order.

If we cannot do so, then return the list [-1].



Example 1:

Input:
    root = [1,2], voyage = [2,1]
Output:
    [-1]

Example 2:

Input:
    root = [1,2,3], voyage = [1,3,2]
Output:
    [1]

Example 3:

Input:
    root = [1,2,3], voyage = [1,2,3]
Output:
    []

Note:
    1 <= N <= 100
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        res = []

        def helper(root, nums):
            if root is None and len(nums) == 0:
                return True
            elif root is None or len(nums) == 0:
                return False
            if root.val != nums[0]:
                return False
            if root.left is None:
                return helper(root.right, nums[1:])
            elif root.right is None:
                return helper(root.left, nums[1:])
            else:
                if root.left.val not in nums[1:] or root.right.val not in nums[1:]:
                    return False
                li, ri = nums.index(root.left.val), nums.index(root.right.val)
                if li == 1:
                    return helper(root.left, nums[1:ri]) and helper(root.right, nums[ri:])
                else:
                    res.append(root.val)
                    return helper(root.right, nums[1:li]) and helper(root.left, nums[li:])

        if helper(root, voyage):
            return res
        else:
            return [-1]


examples = [
    {
        "input": {
            "root": [1, 2],
            "voyage": [2, 1]
        },
        "output": [-1]
    }, {
        "input": {
            "root": [1, 2, 3],
            "voyage": [1, 3, 2]
        },
        "output": [1]
    }, {
        "input": {
            "root": [1, 2, 3],
            "voyage": [1, 2, 3]
        },
        "output": []
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
