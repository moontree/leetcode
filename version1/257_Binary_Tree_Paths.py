"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]

"""
from tree_helper import *


def binary_tree_paths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [str(root.val)]
    res = []
    if root.left:
        res += [str(root.val) + "->" + p for p in binary_tree_paths(root.left)]
    if root.right:
        res += [str(root.val) + "->" + p for p in binary_tree_paths(root.right)]
    return res


def dfs(root, pre, res):
    if root.left is None and root.right is None:
        pre.append(str(root.val))
        res.append(pre[:])
    else:
        pre.append(str(root.val))
        if root.left:
            dfs(root.left, pre, res)
            pre.pop()
        if root.right:
            dfs(root.right, pre, res)
            pre.pop()


examples = [
    {
        "nums": [1, 2, 3],
    }, {
        "nums": [1, 2, 3, None, 5],
    }
]


for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print binary_tree_paths(tr)
