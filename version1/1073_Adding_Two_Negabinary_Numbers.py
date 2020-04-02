"""
Given two numbers arr1 and arr2 in base -2,
return the result of adding them together.

Each number is given in array format:
as an array of 0s and 1s, from most significant bit to least significant bit.

For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.
A number arr in array format is also guaranteed to have no leading zeros:
either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format:
as an array of 0s and 1s with no leading zeros.



Example 1:

Input:
    arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output:
    [1,0,0,0,0]
Explanation:
    arr1 represents 11, arr2 represents 5, the output represents 16.

Note:
    1 <= arr1.length <= 1000
    1 <= arr2.length <= 1000
    arr1 and arr2 have no leading zeros
    arr1[i] is 0 or 1
    arr2[i] is 0 or 1
"""


class Solution(object):
    def addNegabinary(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        c = 0
        res = []
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        i = 0

        def helper(v):
            if v == 0 or v == 1:
                return [0, v]
            elif v == -1:
                return [1, 1]
            elif tmp == 3:
                return [-1, 1]
            elif tmp == 2:
                return [-1, 0]

        while i < len(arr1) and i < len(arr2):
            tmp = arr1[i] + arr2[i] + c
            c, v = helper(tmp)
            res.append(v)
            i += 1
        while i < len(arr1):
            tmp = arr1[i] + c
            c, v = helper(tmp)
            res.append(v)
            i += 1
        while i < len(arr2):
            tmp = arr2[i] + c
            c, v = helper(tmp)
            res.append(v)
            i += 1
        if c == 1:
            res.append(1)
        elif c == -1:
            res.append(1)
            res.append(1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]


examples = [
    {
        "input": {
            "arr1": [1, 1, 1, 1, 1],
            "arr2": [1, 0, 1]
        },
        "output": [1, 0, 0, 0, 0]
    }, {
        "input": {
            "arr1": [1, 1],
            "arr2": [1]
        },
        "output": [0]
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
