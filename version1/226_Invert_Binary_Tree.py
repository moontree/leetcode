"""
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""


def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root
