"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia:
The lowest common ancestor is defined between two nodes v and w as the lowest node in T
that has both v and w as descendants
(where we allow a node to be a descendant of itself).
        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3.
 Another example is LCA of nodes 5 and 4 is 5,
 since a node can be a descendant of itself according to the LCA definition.
"""
from tree_helper import *


def lowest_common_ancestor(root, p, q):
    """
    :type root.val: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q):
        return root
    left, right = lowest_common_ancestor(root.left, p, q), lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


examples = [
    {
        "nums": [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4, None, None],
        "p": 2,
        "q": 7
    }, {
        "nums": [1, 2, 3, None, 4],
        "p": 3,
        "q": 4
    }
]


for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print lowest_common_ancestor(tr, TreeNode(example["p"]), TreeNode(example["q"]))
