"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    stack = []
    res = []
    current = root
    while current or len(stack):
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res


def is_valid_bst(root, less_than = float("inf"), larger_than = float("-inf")):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    if root.val >= less_than or root.val <= larger_than:
        return False
    return is_valid_bst(root.left, min(less_than, root.val), larger_than) and \
           is_valid_bst(root.right, less_than, max(larger_than, root.val))
