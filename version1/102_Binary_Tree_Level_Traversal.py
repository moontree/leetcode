"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from tree_helper import *


def level_order(root):
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
            res.append(current_val[:])
            current_val = []
            height += 1
    if len(current_val):
        res.append(current_val[:])
    return res


examples = [
    {
        "vals": [3, 9, 20, None, None, 15, 7]
    }, {
        "vals": [None]
    }
]


for example in examples:
    print "----"
    tree_root = generate_tree_from_array(example["vals"])
    print level_order(tree_root)
