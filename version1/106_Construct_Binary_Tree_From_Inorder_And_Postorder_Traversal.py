"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

from tree_helper import *


def build_tree(inorder, postorder):
    """
    :type inorder: List[int]
    :type postorder: List[int]
    :rtype: TreeNode
    """
    if len(inorder) == 0:
        return None
    else:
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = build_tree(inorder[: i], postorder[: i])
        root.right = build_tree(inorder[i + 1:], postorder[i: -1])
        return root


examples = [
    {
        "postorder": [9, 15, 7, 20, 3],
        "inorder": [9, 3, 15, 20, 7]
    }, {
        "postorder": [2, 1],
        "inorder": [2, 1]
    }
]


for example in examples:
    print "----"
    res = build_tree(example["inorder"], example["postorder"])
    print_tree(res)
