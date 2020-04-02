"""
Given a fixed length array arr of integers, duplicate each occurrence of zero,
shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place,
do not return anything from your function.



Example 1:

Input:
    [1,0,2,3,0,4,5,0]
Output:
    null
Explanation:
    After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input:
    [1,2,3]
Output:
    null
Explanation:
    After calling your function, the input array is modified to: [1,2,3]


Note:

    1 <= arr.length <= 10000
    0 <= arr[i] <= 9
"""


class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        pairs = []
        cur = 0
        for i, v in enumerate(arr):
            if v == 0:
                pairs.append([cur, 0])
                pairs.append([cur + 1, 0])
                cur += 2
            else:
                pairs.append([cur, v])
                cur += 1
            if cur > len(arr):
                break
        for i, v in pairs:
            if i < len(arr):
                arr[i] = v
        return arr


examples = [
    {
        "input": {
            "arr": [1, 0, 2, 3, 0, 4, 5, 0],
        },
        "output": [1, 0, 0, 2, 3, 0, 0, 4]
    }, {
        "input": {
            "arr": [1, 2, 3],
        },
        "output": [1, 2, 3]
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
