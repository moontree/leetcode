"""
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""
from tree_helper import *


def flatten(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if root is None:
        return root
    stack = [root]
    previous = None
    while len(stack):
        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        if previous is None:
            previous = root
        else:
            previous.left = None
            previous.right = cur
            previous = cur


examples = [
    {
        "nums": [1, 2, 3, 4, 5]
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    # draw_tree(tree)
    flatten(tree)
    draw_tree(tree)
