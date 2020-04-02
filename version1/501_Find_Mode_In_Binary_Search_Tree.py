"""
Given a binary search tree (BST) with duplicates,
find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space?
(Assume that the implicit stack space incurred due to recursion does not count).
"""
from tree_helper import *


def find_mode(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    records = {}

    def traverse(node):
        if node is None:
            return
        records[node.val] = records.get(node.val, 0) + 1
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    res, count = [], 0
    for k in records:
        if records[k] > count:
            res, count = [k], records[k]
        elif records[k] == count:
            res.append(k)
    return res


examples = [
    {
        "nums": [1, None, 2, None, None, 1],
        "res": 2
    }
]


for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print find_mode(tr)