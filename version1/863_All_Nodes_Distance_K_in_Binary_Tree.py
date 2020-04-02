"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.
  The answer can be returned in any order.



Example 1:

Input:
    root = [3,5,1,6,2,0,8,null,null,7,4],
    target = 5, K = 2

Output:
    [7,4,1]

Explanation:
    The nodes that are a distance 2 from the target node (with value 5)
    have values 7, 4, and 1.

    Note that the inputs "root" and "target" are actually TreeNodes.
    The descriptions of the inputs above are just serializations of these objects.


Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        cache = {}

        def coding(cur, prefix):
            if cur:
                cache[cur.val] = [prefix, cur]
                coding(cur.left, prefix + '0')
                coding(cur.right, prefix + '1')

        def dis(s, t):
            ls, lt = len(s), len(t)
            l = min(ls, lt)
            i = 0
            while i < l and s[i] == t[i]:
                i += 1
            return len(s[i:]) + len(t[i:])

        coding(root, '1')
        # print(cache)
        res = []
        target_code = cache[target.val][0]
        for val in cache:
            cod = cache[val][0]
            # print(cod, target_code, dis(cod, target_code))
            if dis(cod, target_code) == K:
                res.append(val)
        return res