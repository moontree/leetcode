"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia:
The lowest common ancestor is defined between two nodes v and w
as the lowest node in T that has both v and w as descendants.
we allow a node to be a descendant of itself

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2,
since a node can be a descendant of itself according to the LCA definition.
"""
from tree_helper import *


def lowest_common_ancestor(root, p, q):
    """
    :type root: TreeNode
    :type p: int
    :type q: int
    :rtype: TreeNode
    """
    cur = root
    l, r = p, q
    if r < l:
        l, r = r, l
    while cur:
        if r < cur.val:
            cur = cur.left
        elif l > cur.val:
            cur = cur.right
        else:
            return cur.val


examples = [
    {
        "nums": [6, 2, 8, 0, 4, 7, 9, 3, 5],
        "p": 2,
        "q": 4,
        "res": 2
    }, {
        "nums": [6, 2, 8, 0, 4, 7, 9, 3, 5],
        "p": 0,
        "q": 3,
        "res": 6
    }, {
        "nums": [2, 1],
        "p": 2,
        "q": 1,
        "res": 2
    }
]


for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print lowest_common_ancestor(tr, example["p"], example["q"])
