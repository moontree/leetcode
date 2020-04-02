"""
=========================
Project -> File: leetcode -> tree_helper.py
Author: zhangchao
=========================
"""

from graphviz import Digraph


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def generate_tree_from_arr(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    q = [root]
    i = 1
    while i < len(arr) and q:
        cur = q.pop(0)
        if arr[i] is not None:
            cur.left = TreeNode(arr[i])
            q.append(cur.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            cur.right = TreeNode(arr[i])
            q.append(cur.right)
        i += 1
    return root


def print_tree(root):
    q = [root]
    res = []
    while q:
        cur = q.pop(0)
        res.append(cur.val if cur else None)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return res


def draw_tree(root):
    dot = Digraph(comment='Tree')
    q = [[root, 0]]
    dot.node('0', str(root.val) if root else 'N')
    res = []
    while q:
        cur, idx = q.pop(0)
        print cur, idx
        res.append(cur.val if cur else None)
        left_idx, right_idx = 2 * idx + 1, 2 * idx + 2
        dot.node(str(left_idx), str(cur.left.val) if cur.left else 'N')
        dot.node(str(right_idx), str(cur.right.val) if cur.right else 'N')
        dot.edge(str(idx), str(left_idx))
        dot.edge(str(idx), str(right_idx))
        if cur.left:
            q.append([cur.left, left_idx])
        if cur.right:
            q.append([cur.right, right_idx])

    dot.view()


if __name__ == '__main__':
    root = generate_tree_from_arr([1, None, 2, None, 3, 4, None])
    print_tree(root)
    draw_tree(root)