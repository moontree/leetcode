"""
Given an array of integers A, find the number of triples of indices (i, j, k) such that:

0 <= i < A.length
0 <= j < A.length
0 <= k < A.length
A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.


Example 1:

Input:
    [2, 1, 3]
Output:
    12
Explanation:
    We could choose the following i, j, k triples:
    (i=0, j=0, k=1) : 2 & 2 & 1
    (i=0, j=1, k=0) : 2 & 1 & 2
    (i=0, j=1, k=1) : 2 & 1 & 1
    (i=0, j=1, k=2) : 2 & 1 & 3
    (i=0, j=2, k=1) : 2 & 3 & 1
    (i=1, j=0, k=0) : 1 & 2 & 2
    (i=1, j=0, k=1) : 1 & 2 & 1
    (i=1, j=0, k=2) : 1 & 2 & 3
    (i=1, j=1, k=0) : 1 & 1 & 2
    (i=1, j=2, k=0) : 1 & 3 & 2
    (i=2, j=0, k=1) : 3 & 2 & 1
    (i=2, j=1, k=0) : 3 & 1 & 2

Note:
    1 <= A.length <= 1000
    0 <= A[i] < 2^16
"""


class Solution(object):
    def countTriplets(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mem = [0] * 65536
        mask = (1 << 16) - 1
        for num in A:
            mk = mask ^ num
            i = mk
            while i:
                mem[i] += 1
                i = (i - 1) & mk
            mem[0] += 1
        res = 0
        for n1 in A:
            for n2 in A:
                res += mem[n1 & n2]
        return res


examples = [
    {
        "input": {
            "A": [2, 1, 3],
        },
        "output": 12
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
