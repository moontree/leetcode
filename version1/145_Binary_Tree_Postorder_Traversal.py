"""
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],

   1
    \
     2
    /
   3


return [3,2,1].
"""
from tree_helper import *


def postorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack, curr = [], [], root
    while curr or len(stack):
        if curr:
            while curr:
                stack.append([curr, 1])
                curr = curr.left
        curr, flag = stack.pop()
        if flag == 1:
            stack.append([curr, 2])
            curr = curr.right
        if flag == 2:
            res.append(curr.val)
            curr = None
    return res


examples = [
    {
        "nums": [1, None, 2, None, None, 3, None]
    }, {
        "nums": [1, 2, 3, 4, 5, 6, 7]
    }, {
        "nums": [1, 2, 3]
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print postorder_traversal(tree)
