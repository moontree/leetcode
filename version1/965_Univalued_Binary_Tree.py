"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Note:

    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        q = [root]
        val = root.val
        while q:
            cur = q.pop(0)
            if cur.val != val:
                return False
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return True
