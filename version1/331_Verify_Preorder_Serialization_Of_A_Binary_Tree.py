"""
One way to serialize a binary tree is to use pre-order traversal.
 When we encounter a non-null node, we record the node's value.
 If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#",
 where # represents a null node.

Given a string of comma separated values,
verify whether it is a correct preorder traversal serialization of a binary tree.
Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid,
 for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false

"""
from tree_helper import *


def is_valid_serialization(preorder):
    """
    :type preorder: str
    :rtype: bool
    """
    # remember how many empty slots we have
    # non-null nodes occupy one slot but create two new slots
    # null nodes occupy one slot

    p = preorder.split(',')

    # initially we have one empty slot to put the root in it
    slot = 1
    for node in p:

        # no empty slot to put the current node
        if slot == 0:
            return False

        # a null node?
        if node == '#':
            # ocuppy slot
            slot -= 1
        else:
            # create new slot
            slot += 1

    # we don't allow empty slots at the end
    return slot == 0


examples = [
    {
        "preorder": "9,3,4,#,#,1,#,#,2,#,6,#,#",
        "res": True
    }, {
        "preorder": "1,#",
        "res": False
    }, {
        "preorder": "9,#,#,1",
        "res": False
    },
]


for example in examples:
    print is_valid_serialization(example["preorder"])