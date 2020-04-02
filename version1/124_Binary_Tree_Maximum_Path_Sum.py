"""
Given a binary tree, find the maximum path sum.

For this problem,
a path is defined as any sequence of nodes from some starting node to any node
 in the tree along the parent-child connections.
 The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""
### helper is the max value from left_tree, right_tree with root


from tree_helper import *


global max_sum
def max_path_sum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    sum_helper(root)
    return max_sum


def sum_helper(root):
    if root is None:
        return 0
    left_sum, right_sum = sum_helper(root.left), sum_helper(root.right)
    with_root = left_sum + root.val + right_sum
    global max_sum
    max_sum = max(with_root, max_sum)
    return max(left_sum, right_sum, 0) + root.val


examples = [
    {
        "vals": [1, 2, 3],
        "res": 6
    }, {
        "vals": [6, -1, None, 5, 1],
        "res": 10
    }
]


for example in examples:
    tree = generate_tree_from_array(example["vals"])
    max_sum = -float("inf")
    print max_path_sum(tree)
