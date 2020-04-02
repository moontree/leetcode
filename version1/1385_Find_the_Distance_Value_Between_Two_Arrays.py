"""
=========================
Project -> File: leetcode -> 1385_Find_the_Distance_Value_Between_Two_Arrays.py
Author: zhangchao
=========================
Given two integer arrays arr1 and arr2, and the integer d,
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i]
such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:

Input:
    arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output:
    2
Explanation:
    For arr1[0]=4 we have:
        |4-10|=6 > d=2
        |4-9|=5 > d=2
        |4-1|=3 > d=2
        |4-8|=4 > d=2
    For arr1[1]=5 we have:
        |5-10|=5 > d=2
        |5-9|=4 > d=2
        |5-1|=4 > d=2
        |5-8|=3 > d=2
    For arr1[2]=8 we have:
        |8-10|=2 <= d=2
        |8-9|=1 <= d=2
        |8-1|=7 > d=2
        |8-8|=0 <= d=2

Example 2:

Input:
    arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output:
    2

Example 3:

Input:
    arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output:
    1

Constraints:

    1 <= arr1.length, arr2.length <= 500
    -10^3 <= arr1[i], arr2[j] <= 10^3
    0 <= d <= 100
"""


class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        cnts = [0 for _ in range(2001)]
        for n in arr2:
            cnts[n + 1000] += 1
        for i in range(1, 2001):
            cnts[i] += cnts[i - 1]
        res = 0
        for n in arr1:
            v1, v2 = n + 1000 - d, n + 1000 + d
            l = cnts[v1 - 1] if v1 > 0 else 0
            r = cnts[v2] if v2 < 2001 else cnts[-1]
            if l == r:
                res += 1
        return res


examples = [
    {
        "input": {
            "arr1": [4, 5, 8],
            "arr2": [10, 9, 1, 8],
            "d": 2
        },
        "output": 2
    },  {
        "input": {
            "arr1": [1, 4, 2, 3],
            "arr2": [-4, -3, 6, 10, 20, 30],
            "d": 3
        },
        "output": 2
    },  {
        "input": {
            "arr1": [2, 1, 100, 3],
            "arr2": [-5, -2, 10, -3, 7],
            "d": 6
        },
        "output": 1
    },  {
        "input": {
            "arr1": [-636, -388, -114, 100, -677, -901, 463, 765, 367, -494, -483, 592, -869, 396, 973, -86, 655, -120, 124, -488,
         108, -101, 743, 101, -72, -978, -190, 712, -307, -649, -472, -6, -951, 624, 323, 910, -147, 999, 168, -962,
         -873, 416, -274, 187, -717, 215, -744, -717, -470, 697, -433, -186, 155, -179, -648, 254, -818, -522, -5, -985,
         -637, 82, -351, 25, 828, 328, 885, -103, 904, 405, 308, 497, -538, -512, -360, 13, 406, -20, 958, -540, 459,
         -156, -310, 147, 251, 857, 491, 879, 338, -437, 991, 323, -551, -902, 887, -854, 563, 47],
            "arr2": [321, 796, -245, -674, 47, 568, 622, 808, -583, -362, -389, 418, -387, 738, 131, -239, -662, 436, 436, 508, -49,
         217, -826, 753, -748, 836, 241, 966, 52, 169, -228, -639, -681, -487, -127, -555],
            "d": 72
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
