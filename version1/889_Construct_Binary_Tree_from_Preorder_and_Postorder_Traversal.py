"""
Return any binary tree that matches the given preorder and postorder traversals.

Values in the traversals pre and post are distinct positive integers.



Example 1:

Input:
    pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
Output:
    [1,2,3,4,5,6,7]


Note:

    1 <= pre.length == post.length <= 30
    pre[] and post[] are both permutations of 1, 2, ..., pre.length.
    It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_helper import *


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if len(pre) == 0:
            return None
        node = TreeNode(pre[0])
        if len(pre) == 1:
            return node
        j = 0
        while j < len(pre) and post[j] != pre[1]:
            j += 1
        node.left = self.constructFromPrePost(pre[1: j + 2], post[: j + 1])
        node.right = self.constructFromPrePost(pre[j + 2:], post[j + 1: -1])
        return node


examples = [
    {
        "input": {
            "pre": [1, 2, 4, 5, 3, 6, 7],
            "post": [4, 5, 2, 6, 7, 3, 1]
        },
        "output": [1, 2, 3, 4, 5, 6, 7]
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
        print_tree(v)