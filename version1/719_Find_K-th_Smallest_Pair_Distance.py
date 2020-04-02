"""
Given an integer array, return the k-th smallest distance among all the pairs.
 The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0
Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.

"""

import heapq
import sys
import bisect

class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, nums[-1] - nums[0]

        def count(d):
            ans = 0
            for i in range(len(nums) - 1):
                r = bisect.bisect_right(nums, nums[i] + d)
                ans += r - i - 1
            return ans
        for i in range(r + 1):
            print i, count(i)
        while l < r:
            mid = (l + r) / 2
            curr = count(mid)
            if curr < k:
                l = mid + 1
            else:
                r = mid

        return l


examples = [
    {
        "input": {
            "nums": [1, 5, 1, 6],
            "k": 4
        },
        "output": 4
    },{
        "input": {
            "nums": [62, 100, 4],
            "k": 2
        },
        "output": 58
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']