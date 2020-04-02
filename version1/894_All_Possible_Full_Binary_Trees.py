"""
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.
Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output: [
[0,0,0,null,null,0,0,null,null,0,0],
[0,0,0,null,null,0,0,0,0],
[0,0,0,0,0,0,0],
[0,0,0,0,0,null,null,null,null,0,0],
[0,0,0,0,0,null,null,0,0]
]
Explanation:

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_helper import *


class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        cache = {
            1: [TreeNode(0)]
        }
        for j in range(3, N + 1, 2):
            res = []
            for i in range(1, j, 2):
                for nl in cache.get(i, []):
                    for nr in cache.get(j - 1 - i, []):
                        node = TreeNode(0)
                        node.left = nl
                        node.right = nr
                        res.append(node)
            cache[j] = res
        return cache.get(N, [])


examples = [
    {
        "input": {
            "N": 7,
        },
        "output": 3
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
        for n in v:
            print_tree(n)
        # print v, v == example['output'], end - start

