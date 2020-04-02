"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem,
 a height-balanced binary tree is defined as a binary tree
 in which the depth of the two subtrees of
 every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from tree_helper import *


def sorted_array_to_BST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if len(nums) == 0:
        return None
    else:
        mid = len(nums) / 2
        root = TreeNode(nums[mid])
        root.left = sorted_array_to_BST(nums[: mid])
        root.right = sorted_array_to_BST(nums[mid + 1:])
        return root


examples = [
    {
        "nums": [-10, -3, 0, 5, 9]
    }
]


for example in examples:
    print "----"
    tree = sorted_array_to_BST(example["nums"])
    print_tree(tree)
