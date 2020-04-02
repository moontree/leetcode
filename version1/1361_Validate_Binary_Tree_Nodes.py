"""
=========================
Project -> File: leetcode -> 1361_Validate_Binary_Tree_Nodes.py
Author: zhangchao
=========================
You have n binary tree nodes numbered from 0 to n - 1
where node i has two children leftChild[i] and rightChild[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:
Input:
    n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output:
    true

Example 2:

Input:
    n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output:
    false

Example 3:

Input:
    n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output:
    false

Example 4:

Input:
    n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
Output:
    false


Constraints:

    1 <= n <= 10^4
    leftChild.length == rightChild.length == n
    -1 <= leftChild[i], rightChild[i] <= n - 1
"""


class DSU:

    def __init__(self, n):
        self.cache = {i: i for i in xrange(n)}

    def find(self, x):
        if self.cache[x] != x:
            self.cache[x] = self.find(self.cache[x])
        return self.cache[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.cache[b] = a


class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        dsu = DSU(n)
        for i in range(n):
            l, r = leftChild[i], rightChild[i]
            if l != -1:
                if dsu.cache[l] != l:
                    return False
                if l == dsu.find(i):
                    return False
                dsu.union(i, l)
            if r != -1:
                if dsu.cache[r] != r:
                    return False
                if r == dsu.find(i):
                    return False
                dsu.union(i, r)
        return sum([i == dsu.cache[i] for i in range(n)]) == 1


examples = [
    {
        "input": {
            "n": 4,
            "leftChild": [1, -1, 3, -1],
            "rightChild": [2, -1, -1, -1]
        },
        "output": True
    }, {
        "input": {
            "n": 4,
            "leftChild": [1, -1, 3, -1],
            "rightChild": [2, 3, -1, -1]
        },
        "output": False
    }, {
        "input": {
            "n": 2,
            "leftChild": [1, 0],
            "rightChild": [-1, -1]
        },
        "output": False
    }, {
        "input": {
            "n": 6,
            "leftChild": [1, -1, -1, 4, -1, -1],
            "rightChild": [2, -1, -1, 5, -1, -1]
        },
        "output": False
    }, {
        "input": {
            "n": 4,
            "leftChild": [1, 2, 0, -1],
            "rightChild": [-1, -1, -1, -1]
        },
        "output": False
    }
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
