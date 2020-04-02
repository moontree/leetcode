"""
Serialization is the process of converting a data structure or object into a sequence of bits
so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary search tree can be serialized to a string
and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

Note: Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.

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