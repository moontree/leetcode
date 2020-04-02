"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
from tree_helper import *


def is_balanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if depth(root) == -1:
        return False
    return True


def depth(root):
    if root is None:
        return 0
    else:
        left_height = depth(root.left)
        right_height = depth(root.right)
        true_height = max(left_height, right_height) + 1
        if left_height == -1 or right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return true_height


examples = [
    {
        "nums": [3, 9, 20, None, None, 15, 7],
        "res": True
    }, {
        "nums": [1, 2, 2, 3, 3, None, None, 4, 4],
        "res": False
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print is_balanced(tree)
