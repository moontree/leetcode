"""
Given an array of integers arr,
write a function that returns true if and only if the number of occurrences of each value in the array is unique.


Example 1:

Input:
    arr = [1,2,2,1,1,3]
Output:
    true
Explanation:
    The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

Input:
    arr = [1,2]
Output:
    false

Example 3:

Input:
    arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output:
    true


Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000
"""


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cache = {}
        for v in arr:
            cache[v] = cache.get(v, 0) + 1
        return len(cache.values()) == len(set(cache.values()))


examples = [
    {
        "input": {
            "arr": [1, 2, 2, 1, 1, 3],
        },
        "output": True
    }, {
        "input": {
            "arr": [1, 2],
        },
        "output": False
    }, {
        "input": {
            "arr": [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0],
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
