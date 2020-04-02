"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
 but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""
from tree_helper import *


def path_sum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """
    count, total, d = 0, 0, {0: 1}
    stack = [(0, root)]
    visited = []
    while stack:
        seen, node = stack.pop()
        if node is None: continue
        if not seen:
            stack += [(1, node), (0, node.right), (0, node.left)]
            total += node.val
            count += d.get(total - sum, 0)
            d[total] = d.get(total, 0) + 1
            visited.append(total)
        else:

            d[visited.pop()] -= 1
            total -= node.val
    return count
