"""
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem,
 a height-balanced binary tree is defined as a binary tree
 in which the depth of the two subtrees of
 every node never differ by more than 1.


Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from list_helper import *
from tree_helper import *


def sorted_list_to_BST(head):
    """
    :type head: ListNode
    :rtype: TreeNode
    """
    if head is None:
        return None
    pre, fast, slow = None, head, head
    while fast and fast.next:
        pre, fast, slow = slow, fast.next.next, slow.next
    root = TreeNode(slow.val)
    if pre:
        pre.next = None
        root.left = sorted_list_to_BST(head)
    root.right = sorted_list_to_BST(slow.next)
    return root


examples = [
    {
        "nums": [-10, -3, 0, 5, 9]
    }, {
        "nums": [-10, -3, 0, 9]
    }
]


for example in examples:
    print "----"
    t_head = generate_list_from_array(example["nums"])
    tree = sorted_list_to_BST(t_head)
    print_tree(tree)
