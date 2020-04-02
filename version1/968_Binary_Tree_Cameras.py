"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.

Example 1:


Input:
    [0,0,null,0,0]
Output:
    1
Explanation:
    One camera is enough to monitor all nodes if placed as shown.


Example 2:

Input:
    [0,0,null,0,null,0,null,null,0]
Output:
    2
Explanation:
    At least two cameras are needed to monitor all nodes of the tree.
    The above image shows one of the valid configurations of camera placement.

Note:

    The number of nodes in the given tree will be in the range [1, 1000].
    Every node has value 0.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def helper(cur):  # placed, visible, not_visible
            if cur is None:
                return [float('inf'), 0, 0]
            lc, rc = helper(cur.left), helper(cur.right)
            # cur placed
            placed = 1 + min(lc) + min(rc)
            # cur visible
            visible = min(lc[0] + min(rc[:2]), min(lc[:2]) + rc[0])
            # not visible
            not_visible = lc[1] + rc[1]
            print (cur.val, [placed, visible, not_visible])
            return [placed, visible, not_visible]

        return min(helper(root)[:2])


examples = [
    {
        "input": {
            "A": [0],
        },
        "output": 1
    }, {
        "input": {
            "A": [1, 2, 3, None, None, None, 4],
        },
        "output": 2
    }, {
        "input": {
            "A": [1, 2, None, 3, 4]
        },
        "output": 1
    }, {
        "input": {
            "A": [0, 0, None, 0, None, 0, None, None,0]
        },
        "output": 2
    }, {
        "input": {
            "A": [0, 0, None, None, 0, 0, None, None, 0, 0]
        },
        "output": 2
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
        root = tree_helper.generate_tree_from_array(example['input']['A'])
        tree_helper.print_tree(root)
        v = func(root)
        end = time.time()
        print v, v == example['output'], end - start
