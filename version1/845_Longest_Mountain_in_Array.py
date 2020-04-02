"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input:
    [2,1,4,7,3,2,5]
Output:
    5
Explanation:
    The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input:
    [2,2,2]
Output:
    0
Explanation:
    There is no mountain.

Note:

    0 <= A.length <= 10000
    0 <= A[i] <= 10000

Follow up:
    Can you solve it using only one pass?
    Can you solve it in O(1) space?
"""


class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        res = 0
        up, down = 0, 0
        prev = A[0]
        for i in range(1, len(A)):
            cur = A[i]
            if cur > prev:
                if down:
                    if up:
                        res = max(res, up + down + 1)
                    down = 0
                    up = 1
                else:
                    up += 1
            elif cur == prev:
                if up and down:
                    res = max(res, up + down + 1)
                else:
                    up = down = 0
            else:
                down += 1
            prev = A[i]
        if up and down:
            res = max(res, up + down + 1)
        return res


examples = [
    {
        "input": {
            "A": [2, 1, 4, 7, 3, 2, 5],
        },
        "output": 5
    }, {
        "input": {
            "A": [2, 2, 2],
        },
        "output": 0
    }, {
        "input": {
            "A": [2, 3],
        },
        "output": 0
    }, {
        "input": {
            "A": [2, 3, 4],
        },
        "output": 0
    }, {
        "input": {
            "A": [1, 2, 0, 2, 0, 2],
        },
        "output": 3
    }, {
        "input": {
            "A": [],
        },
        "output": 0
    },
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
