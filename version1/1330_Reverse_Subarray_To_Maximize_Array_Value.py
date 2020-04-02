"""
=========================
Project -> File: leetcode -> 1330_Reverse_Subarray_To_Maximize_Array_Value.py
Author: zhangchao
=========================
You are given an integer array nums.
The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it.
You can perform this operation only once.

Find maximum possible value of the final array.


Example 1:

Input:
    nums = [2,3,1,5,4]
Output:
    10
Explanation:
    By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.

Example 2:

Input:
    nums = [2,4,9,24,2,1,10]
Output:
    68

Constraints:

    1 <= nums.length <= 3*10^4
    -10^5 <= nums[i] <= 10^5
"""

"""
There are only three cases: 
reverse the prefix subarray, postfix array or the mid subarray.
For the mid case, assuming we are reversing a,b....c,d to a,c...b,d, the difference would be:
|c-a|+|d-b|-|b-a|-|d-c|

So we are trying to maxmize it: 
max(|c-a|+|d-b|-|b-a|-|d-c|) where (c,d) is current pair, 
and (a,b) is the pair in front of it. 
This can be simplified as below removing the abs operators:
    max(c-a+d-b-|b-a|-|d-c|)
    max(c-a+b-d-|b-a|-|d-c|)
    max(a-c+d-b-|b-a|-|d-c|)
    max(a-c+b-d-|b-a|-|d-c|)
we separate (a,b) and (c,d) and (c,d) for current pair is constant and can be moved out of the max operator:
    max(-a-b-|b-a|)+c+d-|d-c|
    max(-a+b-|b-a|)+c-d-|d-c|
    max(a-b-|b-a|)-c+d-|d-c|
    max(a+b-|b-a|)-c-d-|d-c|
and we can keep the record of the history max and thus reduce the two loops into one loop 
(just similar to the optimization in best time to buy and sell stocks):
    mx0=max(-a-b-|b-a|)
    mx1=max(-a+b-|b-a|)
    mx2=max(a-b-|b-a|)
    mx3=max(a+b-|b-a|)
"""

class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return abs(nums[1] - nums[0])
        base, n = 0, len(nums)
        diff_pre, diff_post, diff_mid = -float('inf'), -float('inf'), -float('inf')
        mx0, mx1, mx2, mx3 = float('inf'), float('inf'), float('inf'), float('inf')
        flags_a = [1, 1, -1, -1]
        flags_b = [1, -1, 1, -1]
        for i in range(n - 1):
            diff = abs(nums[i + 1] - nums[i])
            base += diff
            diff_pre = max(diff_pre, abs(nums[i + 1] - nums[0]) - diff)
            diff_post = max(diff_post, abs(nums[i] - nums[-1]) - diff)
        for k in range(4):
            v1, v2 = [], []
            for i in range(n - 1):
                a, b = flags_a[k] * nums[i], flags_b[k] * nums[i + 1]
                diff = abs(nums[i + 1] - nums[i])
                v1.append(a + b - diff)
                v2.append(a + b + diff)
            diff_mid = max(diff_mid, max(v1) - min(v2))
        return base + max(diff_pre, diff_mid, diff_post)


examples = [
    {
        "input": {
            "nums": [2, 3, 1, 5, 4],
        },
        "output": 10
    }, {
        "input": {
            "nums": [2, 5, 1, 4, 3],
        },
        "output": 11
    }, {
        "input": {
            "nums": [2, 5, 1, 3, 4],
        },
        "output": 11
    }, {
        "input": {
            "nums": [2, 4, 9, 24, 2, 1, 10],
        },
        "output": 68
    }, {
        "input": {
            "nums": [93997, 2877, -93018, -76995, -70679],
        },
        "output": 369098
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
