"""
Given a square grid of integers arr,
a falling path with non-zero shifts is a choice of exactly one element from each row of arr,
such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.


Example 1:

Input:
    arr = [[1,2,3],[4,5,6],[7,8,9]]
Output:
    13
Explanation:
    The possible falling paths are:
    [1,5,9], [1,5,7], [1,6,7], [1,6,8],
    [2,4,8], [2,4,9], [2,6,7], [2,6,8],
    [3,4,8], [3,4,9], [3,5,7], [3,5,9]
    The falling path with the smallest sum is [1,5,7], so the answer is 13.


Constraints:

    1 <= arr.length == arr[i].length <= 200
    -99 <= arr[i][j] <= 99
"""


class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """

        def helper(nums):
            m1, m2, i1, i2 = float('inf'), float('inf'), -1, -1
            for i, v in enumerate(nums):
                if v <= m1:
                    m1, m2 = v, m1
                    i1, i2 = i, i1
                elif v < m2:
                    m2, i2 = v, i
            return [m1, i1], [m2, i2]

        r = len(arr)
        cur = arr[0][:]
        for i in range(1, r):
            tmp = arr[i][:]
            (m1, i1), (m2, i2) = helper(cur)
            for j in range(r):
                if j != i1:
                    tmp[j] += m1
                else:
                    tmp[j] += m2
            cur = tmp[:]
        return min(cur)


examples = [
    {
        "input": {
            "arr": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        },
        "output": 13
    }, {
        "input": {
            "arr": [[1]],
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
