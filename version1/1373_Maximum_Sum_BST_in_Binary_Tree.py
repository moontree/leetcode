"""
=========================
Project -> File: leetcode -> 1373_Maximum_Sum_BST_in_Binary_Tree.py
Author: zhangchao
=========================
Given a binary tree root,
the task is to return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Example 1:

Input:
    root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output:
    20
Explanation:
    Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

Example 2:
Input:
    root = [4,3,null,1,2]
Output:
    2
Explanation:
    Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Example 3:

Input:
    root = [-4,-2,-5]
Output:
    0
Explanation:
    All values are negatives. Return an empty BST.

Example 4:

Input:
    root = [2,1,3]
Output:
    6

Example 5:

Input:
    root = [5,4,8,3,null,6,3]
Output:
    7

Constraints:

    Each tree has at most 40000 nodes..
    Each node's value is between [-4 * 10^4 , 4 * 10^4].
"""


class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0

        def helper(cur):
            if cur is None:
                return [True, None, None, 0]

            l, r = helper(cur.left), helper(cur.right)
            if l[0] and r[0]:
                if l[1] is None and r[1] is None:
                    ans = [True, cur.val, cur.val, l[-1] + r[-1] + cur.val]
                elif l[1] is None and cur.val < r[1]:
                    ans = [True, cur.val, r[2], l[-1] + r[-1] + cur.val]
                elif r[1] is None and l[2] < cur.val:
                    ans = [True, l[1], cur.val, l[-1] + r[-1] + cur.val]
                elif l[2] < cur.val < r[1]:
                    ans = [True, l[1], r[2], l[-1] + r[-1] + cur.val]
                else:
                    ans = [False, None, None, None]
                if ans[0]:
                    self.res = max(self.res, ans[-1])
                return ans
            else:
                return [False, None, None, None]

        helper(root)
        return self.res