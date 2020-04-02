# --*-- coding: utf-8 --*--
"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
 Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
import bisect


def next_greater_element(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    records = {}
    pre = []
    for n in nums:
        while pre and pre[-1] < n:
            records[pre[-1]] = n
            pre.pop()
        pre.append(n)
    res = [records.get(v, -1) for v in findNums]
    return res


examples = [
    {
        "input": {
            "findNums": [4, 1, 2],
            "nums": [1, 3, 4, 2]
        },
        "output": [-1, 3, -1]
    }, {
        "input": {
            "findNums": [2, 4],
            "nums": [1, 2, 3, 4]
        },
        "output": [3, -1]
    }
]


for example in examples:
    print next_greater_element(**example["input"])