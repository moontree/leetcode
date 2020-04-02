"""
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.

"""
from tree_helper import *


def count_nodes(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    if lh == rh:
        return (1 << lh) + count_nodes(root.right)
    else:
        return (1 << rh) + count_nodes(root.left)


def height(root):
    if root is None:
        return 0
    return height(root.left) + 1


examples = [
    {
        "nums": [1],
        "res": 1
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print count_nodes(tree)