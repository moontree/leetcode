"""
Given an integer array sorted in non-decreasing order,
there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.



Example 1:

Input:
    arr = [1,2,2,6,6,6,6,7,10]
Output:
    6


Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5
"""


class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr) / 4
        cache = {}
        for v in arr:
            cache[v] = cache.get(v, 0) + 1
            if cache[v] > n:
                return v



examples = [
    {
        "input": {
            "arr": [1, 2, 2, 6, 6, 6, 6, 7, 10],
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
