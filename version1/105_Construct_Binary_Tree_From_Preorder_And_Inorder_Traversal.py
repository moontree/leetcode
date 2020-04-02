"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""

from tree_helper import *


def build_tree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop())
            root.left = build(root.val)
            inorder.pop()
            root.right = build(stop)
            return root
        return None

    preorder.reverse()
    inorder.reverse()
    return build(None)


examples = [
    {
        "preorder": [3, 9, 20, 15, 7],
        "inorder": [9, 3, 15, 20, 7]
    }
]


for example in examples:
    print "----"
    res = build_tree(example["preorder"], example["inorder"])
    print_tree(res)
