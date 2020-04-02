"""
Serialization is the process of converting a data structure or object into a sequence of bits
 so that it can be stored in a file or memory buffer,
 or transmitted across a network connection link to be reconstructed
 later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree.
 There is no restriction on how your serialization/deserialization algorithm should work.
  You just need to ensure that a binary tree can be serialized to a string
   and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
"""
from tree_helper import *


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def to_str(node):
            if node:
                vals.append(str(node.val))
                to_str(node.left)
                to_str(node.right)
            else:
                vals.append('#')
        to_str(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        vals = iter(data.split(","))
        def to_node():
            c = vals.next()
            if c == '#':
                return None
            else:
                node = TreeNode(int(c))
                node.left = to_node()
                node.right = to_node()
                return node
        return to_node()


examples = [
    {
        "nums": [1, 2, 3, None, 4, 5, 6]
    }
]


obj = Codec()
for example in examples:
    tr = generate_tree_from_array(example["nums"])
    print_tree(tr)
    s = obj.serialize(tr)
    print s
    print_tree(obj.deserialize(s))
