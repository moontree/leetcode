"""
Given a binary tree, imagine yourself standing on the right side of it,
 return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
"""
from tree_helper import *


def right_side_view(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    res = []
    cur = root
    stack = []
    depth = 0
    while cur or len(stack):
        while cur:
            if depth > len(res) - 1:
                res.append(cur.val)
            stack.append([cur, depth + 1])
            cur = cur.right
            depth += 1
        cur, depth = stack.pop()
        cur = cur.left
    return res


examples = [
    {
        "nums": [1, 2, 3, None, 5, None, 4],
        "res": [1, 3, 4]
    }, {
        "nums": [1, 2, 3, 4],
        "res": [1, 3, 4]
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print right_side_view(tree)
