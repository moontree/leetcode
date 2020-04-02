"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
from tree_helper import *


def delete_node_while(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    pre, direction, cur = None, None, root
    while cur:
        if key < cur.val:
            pre, direction = cur, "left"
            cur = cur.left
        elif key > cur.val:
            pre, direction = cur, "right"
            cur = cur.right
        else:
            break
    # not found
    if cur is None:
        return root
    # find root
    if pre is None:
        if cur.left is None:
            return cur.right
        elif cur.right is None:
            return cur.left
    # else
    # left is None
    if cur.left is None:
        if direction == "left":
            pre.left = cur.right
        else:
            pre.right = cur.right
    elif cur.right is None: # right is None
        if direction == "left":
            pre.left = cur.left
        else:
            pre.right = cur.left
    else: # find leftmost
        mark = cur
        pre, cur = cur, cur.right
        while cur.left:
            pre, cur = cur, cur.left
        mark.val = cur.val
        if pre == mark:
            pre.right = cur.right
        else:
            pre.left = cur.right
    return root


def delete_node(root, key):
    """
    :type root: TreeNode
    :type key: int
    :rtype: TreeNode
    """
    if root is None:
        return root
    if root.val == key:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            pre, cur = root, root.right
            while cur.left:
                pre, cur = cur, cur.left
            root.val = cur.val
            if pre == root:
                pre.right = cur.right
            else:
                pre.left = cur.right
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:
        root.left = delete_node(root.left, key)
    return root


examples = [
    {
        "nums": [5, 3, 7, 2, 4, None, 9]
    }
]


for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print_tree(delete_node(tr, 5))