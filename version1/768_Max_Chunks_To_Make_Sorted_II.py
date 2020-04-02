"""
=========================
Project -> File: leetcode -> 768_Max_Chunks_To_Make_Sorted_II.py
Author: zhangchao
=========================
This question is the same as "Max Chunks to Make Sorted"
except the integers of the given array are not necessarily distinct,
the input array could be up to length 2000,
and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct),
we split the array into some number of "chunks" (partitions),
and individually sort each chunk.
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input:
    arr = [5,4,3,2,1]
Output:
    1
Explanation:
    Splitting into two or more chunks will not return the required result.
    For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Example 2:

Input:
    arr = [2,1,3,4,4]
Output:
    4
Explanation:
    We can split into two chunks, such as [2, 1], [3, 4, 4].
    However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:
    arr will have length in range [1, 2000].
    arr[i] will be an integer in range [0, 10**8].
"""


class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        q = []
        for i, v in enumerate(arr):
            if q and q[-1] > v:
                head = q.pop()
                while q and q[-1] > v:
                    q.pop()
                q.append(head)
            else:
                q.append(v)
        return len(q)


examples = [
    {
        "input": {
            "arr": [5, 4, 3, 2, 1],
        },
        "output": 1
    }, {
        "input": {
            "arr": [2, 1, 3, 4, 4],
        },
        "output": 4
    }, {
        "input": {
            "arr": [4, 2, 2, 1, 1],
        },
        "output": 1
    }, {
        "input": {
            "arr": [0, 0, 1, 1, 1],
        },
        "output": 5
    }, {
        "input": {
            "arr": [1, 0, 1, 3, 2],
        },
        "output": 3
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
