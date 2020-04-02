"""
=========================
Project -> File: leetcode -> 1356_Sort_Integers_by_The_Number_of_1_Bits.py
Author: zhangchao
=========================
Given an integer array arr.
You have to sort the integers in the array in ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the sorted array.

Example 1:

Input:
    arr = [0,1,2,3,4,5,6,7,8]
Output:
    [0,1,2,4,8,3,5,6,7]
Explantion:
    [0] is the only integer with 0 bits.
    [1,2,4,8] all have 1 bit.
    [3,5,6] have 2 bits.
    [7] has 3 bits.
    The sorted array by bits is [0,1,2,4,8,3,5,6,7]

Example 2:

Input:
    arr = [1024,512,256,128,64,32,16,8,4,2,1]
Output:
    [1,2,4,8,16,32,64,128,256,512,1024]
Explantion:
    All integers have 1 bit in the binary representation, you should just sort them in ascending order.

Example 3:

Input:
    arr = [10000,10000]
Output:
    [10000,10000]

Example 4:

Input:
    arr = [2,3,5,7,11,13,17,19]
Output:
    [2,3,5,17,7,11,13,19]

Example 5:

Input:
    arr = [10,100,1000,10000]
Output:
    [10,100,10000,1000]


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^4
"""


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count(n):
            res = 0
            while n:
                res += (n % 2)
                n /= 2
            return res
        pairs = [[count(v), v] for v in arr]
        pairs.sort()
        return [x[1] for x in pairs]


examples = [
    {
        "input": {
            "arr": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        },
        "output": [0, 1, 2, 4, 8, 3, 5, 6, 7]
    }, {
        "input": {
            "arr": [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1],
        },
        "output": [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    },  {
        "input": {
            "arr": [10000, 10000],
        },
        "output": [10000, 10000]
    },  {
        "input": {
            "arr": [2, 3, 5, 7, 11, 13, 17, 19],
        },
        "output": [2, 3, 5, 17, 7, 11, 13, 19]
    },  {
        "input": {
            "arr": [10, 100, 1000, 10000],
        },
        "output": [10, 100, 10000, 1000]
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
