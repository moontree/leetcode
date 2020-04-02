"""
=========================
Project -> File: leetcode -> 1367_Linked_List_in_Binary_Tree.py
Author: zhangchao
=========================
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head
correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Example 1:

Input:
    head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output:
    true
Explanation:
    Nodes in blue form a subpath in the binary Tree.

Example 2:

Input:
    head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output:
    true

Example 3:

Input:
    head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output:
    false
Explanation:
    There is no path in the binary tree that contains all the elements of the linked list from head.

Constraints:

    1 <= node.val <= 100 for each node in the linked list and binary tree.
    The given linked list will contain between 1 and 100 nodes.
    The given binary tree will contain between 1 and 2500 nodes.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, head, rt):
        if not head:
            return True
        if not rt:
            return False
        if rt.val != head.val:
            return False
        return self.dfs(head.next, rt.left) or self.dfs(head.next, rt.right)

    def isSubPath(self, head, root):
        if not root:
            return False
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)