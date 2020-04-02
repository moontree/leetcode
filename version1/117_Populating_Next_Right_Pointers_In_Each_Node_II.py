"""
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def connect(root):
    start = root
    while start:
        cur = tmp = TreeLinkNode(0)
        while start:
            cur.next = start.left
            if cur.next:
                cur = cur.next
            cur.next = start.right
            if cur.next:
                cur = cur.next
            start = start.next
        start = tmp.next


examples = [
    {
        "vals": [1, 2, 3, None, None, None, 7]
    }
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
