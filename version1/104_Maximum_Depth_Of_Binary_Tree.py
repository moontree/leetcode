"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
from tree_helper import *


def max_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        return max(max_depth(root.left), max_depth(root.right)) + 1


examples = [
    {
        "vals": [3, 9, 20, None, None, 15, 7]
    }, {
        "vals": [None]
    }, {
        "vals": [1, 2, 3, 4, None, None, 5]
    }, {
        "vals": [1, 2, 5]
    }
]


for example in examples:
    print "----"
    tree_root = generate_tree_from_array(example["vals"])
    print max_depth(tree_root)
