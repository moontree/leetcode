"""
Given two arrays A and B of equal size,
the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.


Example 1:

Input:
    A = [2,7,11,15],
    B = [1,10,4,11]
Output:
    [2,11,7,15]


Example 2:

Input:
    A = [12,24,8,32],
    B = [13,25,32,11]
Output:
    [24,32,8,12]


Note:
    1 <= A.length = B.length <= 10000
    0 <= A[i] <= 10^9
    0 <= B[i] <= 10^9

"""


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)
        A.sort()
        bb = [(v, i) for i, v in enumerate(B)]
        bb.sort()
        i, j = 0, 0
        res = [None for _ in range(n)]
        rest = []
        while i < n and j < n:
            if A[i] > bb[j][0]:
                res[bb[j][1]] = A[i]
                i += 1
                j += 1
            else:
                rest.append(A[i])
                i += 1
        i = 0
        for j in range(n):
            if res[j] is None:
                res[j] = rest[i]
                i += 1
        return res


examples = [
    {
        "input": {
            "A": [2, 7, 11, 15],
            "B": [1, 10, 4, 11]
        },
        "output": [2, 11, 7, 15]
    }, {
        "input": {
            "A": [12, 24, 8, 32],
            "B": [13, 25, 32, 11]
        },
        "output": [24, 32, 8, 12]
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
