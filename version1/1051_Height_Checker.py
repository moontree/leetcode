"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to
be standing in non-decreasing order of height.)



Example 1:

Input:
    [1,1,4,2,1,3]
Output:
    3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.


Note:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100
"""


class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        counts = [0 for _ in range(101)]
        for n in heights:
            counts[n] += 1
        target = 0
        res = 0
        for v in heights:
            while counts[target] == 0:
                target += 1
            if v != target:
                res += 1
            counts[target] -= 1
        return res


examples = [
    {
        "input": {
            "heights": [1, 1, 4, 2, 1, 3],
        },
        "output": 3
    }, {
        "input": {
            "heights": [1, 1, 4, 1, 2, 3],
        },
        "output": 4
    }, {
        "input": {
            "heights": [1, 3, 2],
        },
        "output": 2
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
