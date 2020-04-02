"""
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    current = root
    stack = []
    while current or len(stack):
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        res.append(current.val)
        current = current.right
    return res


examples = [
    {
        "vals": [1, None, 2, 3]
    }
]


for example in examples:
    vals = example["vals"]
    e_root = TreeNode(1)
    e_root.right = TreeNode(2)
    e_root.right.left = TreeNode(3)
    print inorder_traversal(e_root)
