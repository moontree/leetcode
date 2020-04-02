"""
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
"""


from tree_helper import *


def sum_of_left_leaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def is_leaf(root):
        if root.left is None and root.right is None:
            return True

    def add_helper(root, res):
        if root is None:
            return
        if root.left:
            if is_leaf(root.left):
                res.append(root.left.val)
            else:
                add_helper(root.left, res)
        if root.right:
            add_helper(root.right, res)

    res = []
    add_helper(root, res)
    return sum(res)


examples = [
    {
        "nums": [3, 9, 20, None, None, 15, 7]
    }
]


for example in examples:
    th = generate_tree_from_array(example["nums"])
    print sum_of_left_leaves(th)
