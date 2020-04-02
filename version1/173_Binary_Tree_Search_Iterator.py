"""
Implement an iterator over a binary search tree (BST).
Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run
 in average O(1) time and uses O(h) memory,
  where h is the height of the tree.
"""
from tree_helper import *


class BSTIterator(object):
    _stack = []

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        cur = root
        while cur:
            self._stack.append(cur)
            cur = cur.left

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self._stack):
            return True
        return False

    def next(self):
        """
        :rtype: int
        """
        cur = self._stack.pop()
        val = cur.val
        cur = cur.right
        while cur:
            self._stack.append(cur)
            cur = cur.left
        return val


tree = generate_tree_from_array([3, 2, 5, 1, None, None, 7])
# Your BSTIterator will be called like this:
i, v = BSTIterator(tree), []
while i.hasNext(): v.append(i.next())
print v