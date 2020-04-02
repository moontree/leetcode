"""
Given a binary tree and a sum,
determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from tree_helper import *


def has_path_sum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if root is None:
        return False
    queue = [[root, root.val]]
    while len(queue):
        current, s = queue.pop(0)
        if s == sum and current.left is None and current.right is None:
            return True
        if current.left:
            queue.append([current.left, s + current.left.val])
        if current.right:
            queue.append([current.right, s + current.right.val])
    return False


examples = [
    {
        "nums": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1],
        "sum": 22
    }, {
        "nums": [-2, None, -3],
        "sum": -5
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print has_path_sum(tree, example["sum"])
