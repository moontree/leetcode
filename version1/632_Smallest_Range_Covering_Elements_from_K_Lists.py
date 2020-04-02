"""
You have k lists of sorted integers in ascending order.
Find the smallest range that includes at least one number from each of the k lists.

We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c if b-a == d-c.


Example 1:

Input:
    [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output:
    [20,24]
Explanation:
List 1:
    [4, 10, 15, 24, 26], 24 is in range [20,24].
List 2:
    [0, 9, 12, 20], 20 is in range [20,24].
List 3:
    [5, 18, 22, 30], 22 is in range [20,24].


Note:

    The given list may contain duplicates, so ascending order means >= here.
    1 <= k <= 3500
    -10^5 <= value of elements <= 10^5.
"""
import heapq


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        maxv = max([x[0] for x in nums])
        q = [[x[0], i, 0] for i, x in enumerate(nums)]
        heapq.heapify(q)
        l, r = q[0][0], maxv
        diff = r - l
        while True:
            tmp_diff = maxv - q[0][0]
            if tmp_diff < diff:
                l, r, diff = q[0][0], maxv, tmp_diff
            v, i, idx = heapq.heappop(q)
            if idx == len(nums[i]) - 1:
                break
            idx += 1
            maxv = max(maxv, nums[i][idx])
            heapq.heappush(q, [nums[i][idx], i, idx])
        return [l, r]


examples = [
    {
        "input": {
            "nums": [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]],
        },
        "output": [20, 24]
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

