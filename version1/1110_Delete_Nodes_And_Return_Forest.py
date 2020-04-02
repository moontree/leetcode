"""
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.



Example 1:

Input:
    root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output:
    [[1,2,null,4],[6],[7]]


Constraints:

    The number of nodes in the given tree is at most 1000.
    Each node has a distinct value between 1 and 1000.
    to_delete.length <= 1000
    to_delete contains distinct values between 1 and 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        vals = {v: True for v in to_delete}
        q = [[root, True]]
        res = []
        i = 0
        while i < len(q):
            cur, flag = q[i]
            if cur.val in vals:
                if cur.left:
                    q.append([cur.left, True])
                if cur.right:
                    q.append([cur.right, True])
                flag = False
            else:
                if cur.left:
                    q.append([cur.left, False])
                    if cur.left.val in vals:
                        cur.left = None
                if cur.right:
                    q.append([cur.right, False])
                    if cur.right.val in vals:
                        cur.right = None
            if flag:
                res.append(cur)
            i += 1
        return res