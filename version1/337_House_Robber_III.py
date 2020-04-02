"""
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
from tree_helper import *


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.rob_helper(root)[1]

    def rob_helper(self, root):
        # return [without, max]
        if root is None:
            return [0, 0]
        l = self.rob_helper(root.left)
        r = self.rob_helper(root.right)
        with_root = root.val + l[0] + r[0]
        without_root = l[1] + r[1]
        return [without_root, max(without_root, with_root)]


examples = [
    {
        "vals": [3, 2, 3, None, 3, None, 1],
        "res": 7
    }, {
        "vals": [3, 4, 5, 1, 3, None, 1],
        "res": 9
    }
]


solution = Solution()
for example in examples:
    tr = generate_tree_from_array(example["vals"])
    print solution.rob(tr)
