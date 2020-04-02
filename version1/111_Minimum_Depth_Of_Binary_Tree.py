"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
from tree_helper import *


def min_depth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    depth = 1
    if root is None:
        return 0
    else:
        queue = [root]
        while True:
            next_level = []
            while len(queue):
                current = queue.pop(0)
                is_leaf = True
                if current.left:
                    next_level.append(current.left)
                    is_leaf = False
                if current.right:
                    next_level.append(current.right)
                    is_leaf = False
                if is_leaf:
                    return depth
            depth += 1
            queue = next_level[:]


examples = [
    {
        "nums": [],
        "res": 0
    }, {
        "nums": [1, 2, 3],
        "res": 2
    }, {
        "nums": [1, None, 2, None, None, 3],
        "res": 2
    }, {
        "nums": [1, 2, 3, None, None, 4, 5],
        "res": 3
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print min_depth(tree)
