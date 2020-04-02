"""
Given an array A of integers,
return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).



Example 1:

Input:
    [3,6,9,12]
Output:
    4
Explanation:
    The whole array is an arithmetic sequence with steps of length = 3.

Example 2:

Input:
    [9,4,7,2,10]
Output:
    3
Explanation:
    The longest arithmetic subsequence is [4,7,10].

Example 3:

Input:
    [20,1,15,3,10,5,8]
Output:
    4
Explanation:
    The longest arithmetic subsequence is [20,15,10,5].


Note:
    2 <= A.length <= 2000
    0 <= A[i] <= 10000
"""


class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cache = {i: {} for i in xrange(len(A))}
        res = 0
        for r in xrange(1, len(A)):
            for l in xrange(r):
                diff = A[r] - A[l]
                cache[r][diff] = cache[l].get(diff, 0) + 1
                res = max(res, cache[r][diff])

        return res + 1


examples = [
    {
        "input": {
            "A": [3, 6, 9, 12],
        },
        "output": 4
    }, {
        "input": {
            "A": [9, 4, 7, 2, 10],
        },
        "output": 3
    }, {
        "input": {
            "A": [20, 1, 15, 3, 10, 5, 8],
        },
        "output": 4
    }, {
        "input": {
            "A": [22,8,57,41,36,46,42,28,42,14,9,43,27,51,0,0,38,50,31,60,29,31,20,23,37,53,27,1,47,42,28,31,10,35,39,12,15,6,35,31,45,21,30,19,5,5,4,18,38,51,10,7,20,38,28,53,15,55,60,56,43,48,34,53,54,55,14,9,56,52],
        },
        "output": 6
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
