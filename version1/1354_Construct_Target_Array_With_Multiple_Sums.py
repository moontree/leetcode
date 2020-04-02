"""
=========================
Project -> File: leetcode -> 1354_Construct_Target_Array_With_Multiple_Sums.py
Author: zhangchao
=========================
Given an array of integers target.
From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.


Example 1:

Input:
    target = [9,3,5]
Output:
    true
Explanation:
    Start with [1, 1, 1]
    [1, 1, 1], sum = 3 choose index 1
    [1, 3, 1], sum = 5 choose index 2
    [1, 3, 5], sum = 9 choose index 0
    [9, 3, 5] Done

Example 2:

Input:
    target = [1,1,1,2]
Output:
    false
Explanation:
    Impossible to create target array from [1,1,1,1].

Example 3:

Input:
    target = [8,5]
Output:
    true


Constraints:

    N == target.length
    1 <= target.length <= 5 * 10^4
    1 <= target[i] <= 10^9
"""
import heapq


class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """

        if len(target) == 1:
            return target[0] == 1
        s, n = sum(target), len(target)
        q = [-v for v in target]
        heapq.heapify(q)

        while True:
            max_val = -heapq.heappop(q)
            if max_val == 1:
                return True
            rest_sum = s - max_val
            pre_val = max_val % rest_sum
            if rest_sum >= max_val or pre_val == 0:
                if rest_sum == 1:
                    return True
                return False
            s = rest_sum + pre_val
            heapq.heappush(q, -pre_val)


examples = [
    {
        "input": {
            "target": [9, 3, 5],
        },
        "output": True
    }, {
        "input": {
            "target": [1, 1, 1, 2],
        },
        "output": False
    }, {
        "input": {
            "target": [8, 5],
        },
        "output": True
    }, {
        "input": {
            "target": [1, 5],
        },
        "output": True
    }, {
        "input": {
            "target": [62305, 12, 1, 1321, 1, 31153, 45, 4577, 16721, 23, 1, 1],
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
