"""
In an array A of 0s and 1s,
how many non-empty subarrays have sum S?



Example 1:

Input:
    A = [1,0,1,0,1], S = 2
Output:
    4
Explanation:
    The 4 subarrays are bolded below:
    1, 0, 1
    1, 0, 1, 0
       0, 1, 0, 1
          1, 0, 1


Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.

"""


class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        if sum(A) < S:
            return 0
        res = 0
        ss, ll, rr = 0, 0, 0
        lz, rz = [0 for _ in range(len(A))], [0 for _ in range(len(A))]
        for i in range(1, len(A)):
            lz[i] = lz[i - 1] + 1 if A[i - 1] == 0 else 0
            idx = len(A) - i - 1
            rz[idx] = rz[idx + 1] + 1 if A[idx + 1] == 0 else 0

        if S == 0:
            for i in range(len(A)):
                if A[i] == 0:
                    res += lz[i] + 1
            return res
        # get ll and rr
        if A[ll] == 0:
            ll += rz[ll] + 1
        rr = ll
        for i in range(S - 1):
            rr += rz[rr] + 1
        while rr < len(A):
            res += (1 + lz[ll]) * (1 + rz[rr])
            ll += rz[ll] + 1
            rr += rz[rr] + 1
        return res


examples = [
    {
        "input": {
            "A": [1, 0, 1, 0, 1],
            "S": 2
        },
        "output": 4
    }, {
        "input": {
            "A": [1, 0, 1, 0, 1],
            "S": 4
        },
        "output": 0
    }, {
        "input": {
            "A": [1, 0, 1, 1],
            "S": 3
        },
        "output": 1
    }, {
        "input": {
            "A": [0, 0, 1, 0, 1, 0, 1, 0],
            "S": 3
        },
        "output": 6
    }, {
        "input": {
            "A": [0, 0, 0, 0, 0],
            "S": 0
        },
        "output": 15
    }, {
        "input": {
            "A": [0, 0, 1, 0, 0],
            "S": 0
        },
        "output": 6
    }, {
        "input": {
            "A": [0, 0, 1, 0, 0],
            "S": 1
        },
        "output": 9
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



