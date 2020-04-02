"""
Given the root of a binary tree,
consider all root to leaf paths:
paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

Example 1:
Input:
    root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output:
    [1,2,3,4,null,null,7,8,9,null,14]

Example 2:

Input:
    root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output:
    [5,4,8,11,null,17,4,7,null,null,null,5]

Example 3:

Input:
    root = [1,2,-3,-5,null,4,null], limit = -1
Output:
    [1,null,-3,4]

Note:

    The given tree will have between 1 and 5000 nodes.
    -10^5 <= node.val <= 10^5
    -10^9 <= limit <= 10^9
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """

        def helper(cur, s):
            if cur is None:
                return [None, False]
            s += cur.val
            if cur.left is None and cur.right is None:
                if s < limit:
                    return [None, False]
                else:
                    return [cur, True]

            valid = False
            if cur.left:
                left = helper(cur.left, s)
                if not left[1]:
                    cur.left = None
                if left[1]:
                    valid = True
            if cur.right:
                right = helper(cur.right, s)
                if not right[1]:
                    cur.right = None
                if right[1]:
                    valid = True
            if not valid:
                cur = None

            return [cur, valid]

        return helper(root, 0)[0]