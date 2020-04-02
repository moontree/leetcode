"""
Given an array of integers A,
a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.



Example 1:

Input:
    [1,2,2]
Output:
    1
Explanation:
    After 1 move, the array could be [1, 2, 3].

Example 2:

Input:
    [3,2,1,2,1,7]
Output:
    6
Explanation:
    After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
    It can be shown with 5 or less moves that it is impossible for the array to have all unique values.


Note:

    0 <= A.length <= 40000
    0 <= A[i] < 40000

"""


class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        parts = []
        s = 0
        for i, n in enumerate(A):
            if A[s] + i - s < n:
                parts.append([s, i])
                s = i
        if s < len(A):
            parts.append([s, len(A)])
        res = 0
        for s, e in parts:
            l = e - s
            start = A[s]
            end = A[s] + l - 1
            res += (start + end) * l / 2
        return res - sum(A)


examples = [
    {
        "input": {
            "A": [1, 2, 2],
        },
        "output": 1
    }, {
        "input": {
            "A": [3, 2, 1, 2, 1, 7],
        },
        "output": 6
    }, {
        "input": {
            "A": [19,15,45,27,48,38,28,13,34,22,36,20,24,1,36,1,34,29,38,14,34,10,26,17,48,48,10,28,16,48,46,29,36,34,17,45,44,16,37,0,40,28,47,18,31,16,39,30,49,0],
        },
        "output": 136
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
