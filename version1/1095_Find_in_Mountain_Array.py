"""
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr,
return the minimum index such that mountainArr.get(index) == target.
If such an index doesn't exist, return -1.

You can't access the mountain array directly.
You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.
Also, any solutions that attempt to circumvent the judge will result in disqualification.


Example 1:

Input:
    array = [1,2,3,4,5,3,1], target = 3
Output:
    2
Explanation:
    3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Example 2:

Input:
    array = [0,1,2,4,2,1], target = 3
Output:
    -1
Explanation:
    3 does not exist in the array, so we return -1.

Constraints:

    3 <= mountain_arr.length() <= 10000
    0 <= target <= 10^9
    0 <= mountain_arr.get(index) <= 10^9
"""


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        l, r = 0, len(mountain_arr) - 1
        mi = -1
        while l <= r:
            mid = (l + r) >> 1
            left, cur = mountain_arr[mid - 1], mountain_arr[mid]
            if left > cur:
                r = mid - 1
            elif mountain_arr[mid + 1] > cur:
                l = mid + 1
            else:
                mi = mid
                break
        print('mountain index', mi)
        # find from left
        l, r = 0, mi
        while l <= r:
            mid = (l + r) >> 1
            cur = mountain_arr[mid]
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        print('left not found')
        # find from right
        l, r = mi, len(mountain_arr) - 1
        while l <= r:
            mid = (l + r) >> 1
            cur = mountain_arr[mid]
            print(l, r, mid, cur, target)
            if cur == target:
                return mid
            elif cur < target:
                r = mid - 1
            else:
                l = mid + 1
        print('right not found')
        return -1


examples = [
    {
        "input": {
            "mountain_arr": [1, 2, 3, 4, 5, 3, 1],
            "target": 3,
        },
        "output": 2
    }, {
        "input": {
            "mountain_arr": [0, 1, 2, 4, 2, 1],
            "target": 3,
        },
        "output": -1
    }, {
        "input": {
            "mountain_arr": [1, 2, 3, 4, 5, 3, 1],
            "target": 2,
        },
        "output": 1
    }, {
        "input": {
            "mountain_arr": [3, 5, 3, 2, 0],
            "target": 0,
        },
        "output": 4
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
