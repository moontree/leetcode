"""
Given a binary search tree,
 write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 <= k <= BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and
you need to find the kth smallest frequently?
 How would you optimize the kthSmallest routine?
"""
from tree_helper import *


def kth_smallest(root, k):
    cur = root
    count = 0
    stack = []
    while cur or len(stack):
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        count += 1
        if count == k:
            return cur.val
        cur = cur.right


def kth_smallest_recursive(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    left_count = count_helper(root.left)
    if left_count == k - 1:
        return root.val
    if left_count < k - 1:
        return kth_smallest_recursive(root.right, k - 1 - left_count)
    else:
        return kth_smallest_recursive(root.left, k)


def count_helper(root):
    if root is None:
        return 0
    left_count = count_helper(root.left)
    right_count = count_helper(root.right)
    return left_count + right_count + 1


def kth_smallest_modify_structure(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    count_helper_modify(root)
    cur = root
    while cur:
        if cur.val[1] == k - 1:
            return cur.val[0]
        if cur.val[1] < k - 1:
            k -= cur.val[1] + 1
            cur = cur.right
        else:
            cur = cur.left


def count_helper_modify(root):
    if root is None:
        return 0
    left_count = count_helper_modify(root.left)
    right_count = count_helper_modify(root.right)
    root.val = [root.val, left_count, right_count]
    return left_count + right_count + 1


examples = [
    {
        "nums": [10, 5, 15, 3, 7],
        "k": 1
    }, {
        "nums": [10, 5, 15, 3, 7],
        "k": 2
    }, {
        "nums": [10, 5, 15, 3, 7],
        "k": 3
    }, {
        "nums": [10, 5, 15, 3, 7],
        "k": 4
    }, {
        "nums": [10, 5, 15, 3, 7],
        "k": 5
    }
]


for example in examples:
    tree = generate_tree_from_array(example["nums"])
    print kth_smallest_modify_structure(tree, example["k"])
    # draw_tree(tree)
