"""
Given an array arr,
replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.


Example 1:

Input:
    arr = [17,18,5,4,6,1]
Output:
    [18,6,6,6,1,-1]

Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i] <= 10^5
"""


class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        v, res = -1, []
        for n in arr[::-1]:
            res.append(v)
            v = max(v, n)
        return res[::-1]


examples = [
    {
        "input": {
            "arr": [17, 18, 5, 4, 6, 1],
        },
        "output": [18, 6, 6, 6, 1, -1]
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
