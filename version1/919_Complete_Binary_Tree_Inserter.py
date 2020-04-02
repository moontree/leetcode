"""
A complete binary tree is a binary tree in which every level,
except possibly the last, is completely filled,
and all nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree
and supports the following operations:

CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;

CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v
so that the tree remains complete, and returns the value of the parent of the inserted TreeNode;

CBTInserter.get_root() will return the head node of the tree.


Example 1:

Input:
    inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
Output:
    [null,1,[1,2]]

Example 2:

Input:
    inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
Output:
    [null,3,4,[1,2,3,4,5,6,7,8]]


Note:
    The initial given tree is complete and contains between 1 and 1000 nodes.
    CBTInserter.insert is called at most 10000 times per test case.
    Every value of a given or inserted node is between 0 and 5000.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.head = root
        q = []
        if root:
            q = [[root, 0]]
            tmp = [root]
            while tmp:
                cur = tmp.pop(0)
                if cur.left:
                    q.append([cur.left, 0])
                    tmp.append(cur.left)
                    q[0][1] = 1
                if cur.right:
                    q.append([cur.right, 0])
                    tmp.append(cur.right)
                    q.pop(0)
        self.q = q

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        cur = self.q[0][0]
        if self.q[0][1] == 0:
            cur.left = TreeNode(v)
            self.q.append([cur.left, 0])
            self.q[0][1] = 1
        elif self.q[0][1] == 1:
            cur.right = TreeNode(v)
            self.q.pop(0)
            self.q.append([cur.right, 0])
        return cur.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.head


examples = [
    {
        "input": {
            "root": [1],
            "inserts": [2]
        },
        "output": [1]
    }, {
        "input": {
            "root": [1, 2, 3, 4, 5, 6],
            "inserts": [7, 8]
        },
        "output": [3, 4]
    }
]


import time
if __name__ == '__main__':

    for example in examples:
        print '----------'
        start = time.time()
        obj = CBTInserter(example['input']['root'])
        for input, res in zip(example['input']['inserts'], example['output']):
            print obj.insert(input) == res
        # end = time.time()
        # print v, v == example['output'], end - start
