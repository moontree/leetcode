"""
Given a binary tree rooted at root,
the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

Example 1:

Input:
    [3,5,1,6,2,0,8,null,null,7,4]
Output:
    [2,7,4]
"""

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        cache = defaultdict(list)

        def helper(root, depth=0):
            if root.left is None and root.right is None:
                cache[depth].append(root)
                return depth
            ld, rd = -1, -1
            if root.left:
                ld = helper(root.left, depth + 1)
            if root.right:
                rd = helper(root.right, depth + 1)
            if ld == rd:
                cache[ld].append(root)
            return max(ld, rd)

        helper(root)

