"""
Given a binary search tree,
rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree,
and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9
Note:

The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from tree_helper import *


class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        cur = root
        q = []
        vals = []
        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            vals.append(cur.val)
            cur = cur.right
        if len(vals):
            head = TreeNode(vals[0])
            cur = head
            for c in vals[1:]:
                cur.right = TreeNode(c)
                cur = cur.right
            return head
        return None


examples = [
    {
        "input": {
            "A": [5,3,6,2,4,None,8,1,None,None,None,7,9],
        },
        "output": True
    }
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        n = generate_tree_from_array(example['input']['A'])
        print_tree(n)
        v = func(n)
        end = time.time()
        print v, v == example['output'], end - start
