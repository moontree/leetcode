"""
Given an integer array arr and a target value target,
return the integer value such that
when we change all the integers larger than value in the given array to be equal to value,
the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie,
return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Example 1:

Input:
    arr = [4,9,3], target = 10
Output:
    3
Explanation:
    When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

Example 2:

Input:
    arr = [2,3,5], target = 10
Output:
    5

Example 3:

Input:
    arr = [60864,25176,27249,21296,20204], target = 56803
Output:
    11361


Constraints:

    1 <= arr.length <= 10^4
    1 <= arr[i], target <= 10^5
"""
import bisect


class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        s, ss = 0, []
        for v in arr:
            s += v
            ss.append(s)
        ss.append(0)

        def helper(t):
            i = bisect.bisect_right(arr, t)
            v = ss[i - 1] + (len(arr) - i) * t
            return v

        l, r, res = 0, max(arr), -1

        while l <= r:
            mid = (l + r) / 2
            if helper(mid) <= target:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        v1 = abs(target - helper(res))
        v2 = abs(target - helper(res + 1))
        return res if v1 <= v2 else res + 1


examples = [
    {
        "input": {
            "arr": [4, 9, 3],
            "target": 10
        },
        "output": 3
    }, {
        "input": {
            "arr": [2, 3, 5],
            "target": 10
        },
        "output": 5
    },  {
        "input": {
            "arr": [60864, 25176, 27249, 21296, 20204],
            "target": 56803
        },
        "output": 11361
    },
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
