"""
Given an array of integers A with even length,
return true if and only if it is possible to reorder it such that
A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.


Example 1:

Input:
    [3,1,3,6]
Output:
    false

Example 2:

Input:
    [2,1,2,6]
Output:
    false

Example 3:

Input:
    [4,-2,2,-4]
Output:
    true
Explanation:
    We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].

Example 4:

Input:
    [1,2,4,16,8,4]
Output:
    false

Note:

    0 <= A.length <= 30000
    A.length is even
    -100000 <= A[i] <= 100000
"""


class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        A.sort()
        counts = {}
        for n in A:
            counts[n] = counts.get(n, 0) + 1
        for v in A:
            if counts[v] == 0:
                continue
            if v < 0:
                vv = v / 2
                if v % 2 == 1 or vv not in counts or counts[vv] == 0:
                    return False
                counts[v / 2] -= 1
                counts[v] -= 1
            elif v >= 0:
                counts[v] -= 1
                vv = v * 2
                if vv not in counts or counts[vv] == 0:
                    return False
                counts[vv] -= 1
        return True


examples = [
    {
        "input": {
            "A": [3, 1, 3, 6],
        },
        "output": False
    }, {
        "input": {
            "A": [2, 1, 2, 6],
        },
        "output": False
    }, {
        "input": {
            "A": [4, -2, 2, -4],
        },
        "output": True
    }, {
        "input": {
            "A": [1, 2, 4, 16, 8, 4],
        },
        "output": False
    }, {
        "input": {
            "A": [0, 0],
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
