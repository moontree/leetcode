"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.
96 : Total number?

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(root):
    stack = [root]
    res = []
    while len(stack):
        current = stack[0]
        if current:
            res.append(current.val)
            stack.append(current.left)
            stack.append(current.right)
        else:
            res.append('None')
        stack = stack[1:]
    print res


def generate_trees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    if n == 0:
        return []
    res = generate_trees_by_array(1, n + 1)
    print res
    for node in res:
        print_tree(node)


def generate_trees_by_array(start, end):
    if start == end:
        return [None]
    else:
        res = []
        for i in range(start, end):
            for l in generate_trees_by_array(start, i):
                for r in generate_trees_by_array(i + 1, end):
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res


generate_trees(1)
