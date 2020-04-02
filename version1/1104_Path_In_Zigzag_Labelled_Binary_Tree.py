"""
In an infinite binary tree where every node has two children,
the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...),
the labelling is left to right,
while in the even numbered rows (second, fourth, sixth,...),
the labelling is right to left.

Given the label of a node in this tree,
 return the labels in the path from the root of the tree to the node with that label.


Example 1:

Input:
    label = 14
Output:
    [1,3,4,14]

Example 2:

Input:
    label = 26
Output:
    [1,2,6,10,26]

Constraints:
    1 <= label <= 10^6
"""
import math


class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        depth = int(math.log(label, 2)) + 1
        base = 1 << (depth - 1)
        idx = base * 3 - label - 1 if depth % 2 == 0 else label
        while depth:
            if depth % 2 == 1:
                label = idx
            else:
                base = 1 << (depth - 1)
                label = base * 3 - idx - 1
            res.append(label)
            idx /= 2
            depth -= 1
        return res[::-1]


examples = [
    {
        "input": {
            "label": 14,
        },
        "output": [1, 3, 4, 14]
    }, {
        "input": {
            "label": 26,
        },
        "output": [1, 2, 6, 10, 26]
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
