"""
Find the kth largest element in an unsorted array.
 Note that it is the kth largest element in the sorted order,
 not the kth distinct element.
For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1<= k <= array's length.
"""
import heapq


def find_kth_largest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    h = []
    for v in nums:
        heapq.heappush(h, v)
    for i in range(len(nums) - k + 1):
        val = heapq.heappop(h)
    return val


examples = [
    {
        "nums": [3, 2, 1, 5, 6, 4],
        "k": 2,
        "res": 5
    }, {
        "nums": [7, 6, 5, 4, 3, 2, 1],
        "k": 5,
        "res": 3
    }
]


for example in examples:
    print find_kth_largest(example["nums"], example["k"])
