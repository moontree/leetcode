"""
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?


"""
from tree_helper import *


def preorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res, stack, curr = [], [], root
    while curr or stack:
        if curr:
            res.append(curr.val)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return res


examples = [
    {
        "nums": [1, None, 2, None, None, 3, None]
    }, {
        "nums": [1, 2, 3, 4, 5, 6, 7]
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print preorder_traversal(tree)
