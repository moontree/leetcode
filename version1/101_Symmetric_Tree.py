"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


from tree_helper import *


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_symmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    return is_mirror(root.left, root.right)


def is_mirror(left, right):
    if left and right:
        if left.val == right.val:
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
        else:
            return False
    if left is None and right is None:
        return True
    else:
        return False


examples = [
    {
        "vals": [1, 2, 2, None, 3, None, 3],
        "res": False
    }, {
        "vals": [1, 2, 2, 3, 4, 4, 3],
        "res": True
    }
]


for example in examples:
    tree = is_symmetric(generate_tree_from_array(example["vals"]))
    print tree
