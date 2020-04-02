"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from tree_helper import *


def path_sum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    res = []
    find_path(root, [], 0, sum, res)
    return res


def find_path(current, previous, previous_sum, sum, res):
    if current:
        if current.left is None and current.right is None:
            if previous_sum + current.val == sum:
                previous.append(current.val)
                res.append(previous[:])
                previous.pop()
        else:
            previous_sum += current.val
            previous.append(current.val)
            find_path(current.left, previous, previous_sum, sum, res)
            find_path(current.right, previous, previous_sum, sum, res)
            previous.pop()
            previous_sum -= current.val


examples = [
    {
        "nums": [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1],
        "sum": 22
    }, {
        "nums": [-2, None, -3],
        "sum": -5
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print path_sum(tree, example["sum"])
