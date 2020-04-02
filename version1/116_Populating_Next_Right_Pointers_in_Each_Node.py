"""
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
You may assume that it is a perfect binary tree
(ie, all leaves are at the same level, and every parent has two children).
For example,
Given the following perfect binary tree,
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    if root is None or root.left is None:
        return
    start = root
    while start:
        cur = start
        start = start.left
        while cur and cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        # head = start
        # while head:
        #     print head.val, '->',
        #     head = head.next
        # print 'None'


examples = [
    {
        "vals": [1, 2, 3, 4, 5, 6, 7]
    },
]


def generate_trees_from_array(vals):
    if len(vals) == 0:
        return None
    nodes = []
    for v in vals:
        if v:
            nodes.append(TreeLinkNode(v))
        else:
            nodes.append(None)
    nums = len(vals)
    for i in range(nums / 2 + 1):
        if nodes[i]:
            if 2 * i + 1 < nums:
                nodes[i].left = nodes[2 * i + 1]
            if 2 * i + 2 < nums:
                nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


for example in examples:
    tree = generate_trees_from_array(example["vals"])
    connect(tree)
