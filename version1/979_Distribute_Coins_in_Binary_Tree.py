"""
Given the root of a binary tree with N nodes,
each node in the tree has node.val coins,
and there are N coins total.

In one move,
we may choose two adjacent nodes and move one coin from one node to another.
(The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.



Example 1:

Input:
    [3,0,0]
Output:
    2
Explanation:
    From the root of the tree,
    we move one coin to its left child,
    and one coin to its right child.

Example 2:

Input:
    [0,3,0]
Output:
    3
Explanation:
    From the left child of the root,
     we move two coins to the root [taking two moves].
     Then, we move one coin from the root of the tree to the right child.

Example 3:

Input:
    [1,0,2]
Output:
    2

Example 4:
Input:
    [1,0,0,null,3]
Output:
    4

Note:

    1<= N <= 100
    0 <= node.val <= N
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(cur):
            if cur is None: # [more than need, less than need]
                return [0, 0]
            else:
                lc, rc = helper(cur.left), helper(cur.right)
                rest = lc[0] + rc[0] - lc[1] - rc[1] + cur.val - 1
                self.res += lc[0] + rc[0] + lc[1] + rc[1]
                if rest > 0:
                    return [rest, 0]
                else:
                    return [0, -rest]
        helper(root)
        return self.res


examples = [
    {
        "input": {
            "A": [3, 0, 0],
        },
        "output": 2
    }, {
        "input": {
            "A": [0, 3, 0],
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 0, 2],
        },
        "output": 2
    }, {
        "input": {
            "A": [1, 0, 0, None, 3],
        },
        "output": 4
    }
]


import tree_helper
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
        # v = func(**example['input'])
        root = tree_helper.generate_tree_from_array(example['input']['A'])
        v = func(root)
        end = time.time()
        print v, v == example['output'], end - start
