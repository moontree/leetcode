"""
Given an array A,
partition it into two (contiguous) subarrays left and right so that:

Every element in left is less than or equal to every element in right.
left and right are non-empty.
left has the smallest possible size.
Return the length of left after such a partitioning.
It is guaranteed that such a partitioning exists.



Example 1:

Input:
    [5,0,3,8,6]
Output:
    3
Explanation:
    left = [5,0,3], right = [8,6]

Example 2:

Input:
    [1,1,1,0,6,12]
Output:
    4
Explanation:
    left = [1,1,1,0], right = [6,12]


Note:

    2 <= A.length <= 30000
    0 <= A[i] <= 10^6
    It is guaranteed there is at least one way to partition A as described.

"""


class Solution(object):
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left_max, cur_max = A[0], 0
        res = 0
        for i in range(1, len(A)):
            v = A[i]
            if v > cur_max:
                cur_max = v
            if v < left_max:
                res = i
                if cur_max > left_max:
                    left_max = cur_max
        return res + 1


examples = [
    {
        "input": {
            "A": [5, 0, 3, 8, 6],

        },
        "output": 3
    }, {
        "input": {
            "A": [1, 1, 1, 0, 6, 12],

        },
        "output": 4
    }, {
        "input": {
            "A": [1, 2],

        },
        "output": 1
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
