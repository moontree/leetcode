"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""
from tree_helper import *


def recover_tree(root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    res, stack, first, second = None, [], None, None
    while True:
        while root:
            stack.append(root)
            root = root.left
        if len(stack) == 0:
            break
        node = stack.pop()
        if res and res.val > node.val:
            if not first:
                first = res
            second = node
        res = node
        root = node.right
    first.val, second.val = second.val, first.val


examples = [
    {
        "nums": [2, 3, 1]
    }, {
        "nums": [5, 3, 7, 2, 9, 6, 4]
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    recover_tree(tree)
    print_tree(tree)
