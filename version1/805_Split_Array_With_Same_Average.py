"""
=========================
Project -> File: leetcode -> 805_Split_Array_With_Same_Average.py
Author: zhangchao
=========================
In a given integer array A,
we must move every element of A to either list B or list C.
(B and C initially start empty.)

Return true if and only if after such a move,
it is possible that the average value of B is equal to the average value of C,
 and B and C are both non-empty.

Example :
Input:
    [1,2,3,4,5,6,7,8]
Output:
    true
Explanation:
    We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

    The length of A will be in the range [1, 30].
    A[i] will be in the range of [0, 10000].

"""


class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return False
        s, n = sum(A), len(A)
        A = [v * n - s for v in A]
        for v in A:
            if v == 0:
                return True
        A.sort()
        left, right = A[: n / 2], A[n / 2:]
        print left, right
        ls, rs = {left[0]: 1}, {right[0]: 1}
        for v in left[1:]:
            tmp = {v: 1}
            for k in ls:
                tmp[k + v] = 1
            ls.update(tmp)

        for v in right[1:]:
            tmp = {v: 1}
            for k in rs:
                tmp[k + v] = 1
            rs.update(tmp)
        if 0 in rs: return True
        sl, sr = sum(left), sum(right)
        for k in ls:
            if k == sl and -k == sr:
                continue
            if -k in rs:
                return True
        return False


examples = [
    {
        "input": {
            "A": [1, 2, 3, 4, 5, 6, 7, 8],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 2],
        },
        "output": False
    }, {
        "input": {
            "A": [5, 3, 11, 19, 2],
        },
        "output": True
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
