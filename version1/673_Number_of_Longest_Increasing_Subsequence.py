# --*-- encoding: utf-8 --*--
"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1,
and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.


"""
"""
1, 4, 5, 5, 3, 4, 5 for example
1
1 4
1 4 5
1 3 
1 3 
1 3 4 
1 3 4 5
"""

import bisect


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        q = []
        cache = [[[-float('inf'), 1]]]

        for i, n in enumerate(nums):
            idx = bisect.bisect(q, n)
            count = 0
            if idx >= len(q):
                if q and q[-1] == n:
                    for v, c in cache[idx - 1]:
                        if v < n:
                            count += c
                        else:
                            break
                    cache[len(q)].insert(0, [n, count])
                else:
                    q.append(n)
                    for v, c in cache[idx]:
                        if v < n:
                            count += c
                        else:
                            break
                    cache.append([[n, count]])
            else:
                if q[idx - 1] == n:
                    for v, c in cache[idx - 1]:
                        if v < n:
                            count += c
                        else:
                            break
                    cache[idx].insert(0, [n, count])
                else:
                    q[idx] = n
                    for v, c in cache[idx]:
                        if v < n:
                            count += c
                        else:
                            break
                    cache[idx + 1].insert(0, [n, count])
        # print cache
        res = 0
        q = cache[-1]
        for v, c in q:
            res += c
        # while q:
        #     tmp = []
        #     for v, i in tmp
        # print(res)
        # print(cache)
        return res


examples = [
    {
        "input": [1, 3, 5, 4, 7],
        "output": 2,
    }, {
        "input": [2, 2, 2, 2, 2],
        "output": 5,
    }, {
        "input": [1, 4, 5, 5, 5, 6],
        "output": 3,
    }, {
        "input": [1, 4, 5, 5, 5, 3, 3, 3, 4, 5],
        "output": 3,
    }, {
        "input": [1, 4, 5, 5, 5, 3, 6],
        "output": 3,
    }, {
        "input": [],
        "output": 0,
    },
]


if __name__ == '__main__':
    solution = Solution()

    for example in examples:
        print solution.findNumberOfLIS(example['input']) == example["output"]