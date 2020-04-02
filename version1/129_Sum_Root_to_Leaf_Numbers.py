"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

"""
from tree_helper import *


class Solution(object):
    def traverse(self, root, v=0):
        """
        :type root: TreeNode
        :type v: int
        """
        if root is None:
            return 0
        v = v * 10 + root.val
        if root.left is None and root.right is None:
            self.res += v
        if root.left:
            self.traverse(root.left, v)
        if root.right:
            self.traverse(root.right, v)

    def sum_numbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        if root is None:
            return 0
        self.traverse(root)
        return self.res


examples = [
    {
        "nums": [1, 2, 3],
        "res": 25
    }
]


solution = Solution()
for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print solution.sum_numbers(tree)
