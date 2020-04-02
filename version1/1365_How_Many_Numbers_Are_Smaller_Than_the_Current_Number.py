"""
=========================
Project -> File: leetcode -> 1365_How_Many_Numbers_Are_Smaller_Than_the_Current_Number.py
Author: zhangchao
=========================
Given the array nums,
for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.


Example 1:

Input:
    nums = [8,1,2,2,3]
Output:
    [4,0,1,1,3]
Explanation:
    For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
    For nums[1]=1 does not exist any smaller number than it.
    For nums[2]=2 there exist one smaller number than it (1).
    For nums[3]=2 there exist one smaller number than it (1).
    For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

Example 2:

Input:
    nums = [6,5,4,8]
Output:
    [2,1,0,3]

Example 3:

Input:
    nums = [7,7,7,7]
Output:
    [0,0,0,0]

Constraints:

    2 <= nums.length <= 500
    0 <= nums[i] <= 100
"""


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cnts = [0 for _ in range(101)]
        for v in nums:
            cnts[v] += 1
        for i in range(1, 101):
            cnts[i] += cnts[i - 1]
        res = []
        for v in nums:
            if v == 0:
                res.append(0)
            else:
                res.append(cnts[v - 1])
        return res


examples = [
    {
        "input": {
            "nums": [8, 1, 2, 2, 3],
        },
        "output": [4, 0, 1, 1, 3]
    }, {
        "input": {
            "nums": [6, 5, 4, 8],
        },
        "output": [2, 1, 0, 3]
    }, {
        "input": {
            "nums": [7, 7, 7, 7],
        },
        "output": [0, 0, 0, 0]
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
