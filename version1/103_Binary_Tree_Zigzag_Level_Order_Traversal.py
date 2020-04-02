"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
 (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from tree_helper import *


def zigzag_level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    stack = []
    if root:
        stack.append([root, 0])
    current_val = []
    height = 0
    while len(stack):
        node = stack[0]
        if height == node[1]:
            current_val.append(node[0].val)
            if node[0].left:
                stack.append([node[0].left, height + 1])
            if node[0].right:
                stack.append([node[0].right, height + 1])
            stack = stack[1:]
        else:
            if height % 2 == 1:
                res.append(current_val[::-1])
            else:
                res.append(current_val[:])
            current_val = []
            height += 1
    if len(current_val):
        if height % 2 == 1:
            res.append(current_val[::-1])
        else:
            res.append(current_val[:])
    return res


examples = [
    {
        "vals": [3, 9, 20, None, None, 15, 7]
    }, {
        "vals": [None]
    }, {
        "vals": [1, 2, 3, 4, None, None, 5]
    }, {
        "vals": [1, 2, 5]
    }
]


for example in examples:
    print "----"
    tree_root = generate_tree_from_array(example["vals"])
    print zigzag_level_order(tree_root)
