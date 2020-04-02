"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 <= k <= number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
import heapq


def top_k_frequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    records = {}
    for n in nums:
        records[n] = records.get(n, 0) + 1
    h = []
    for key in records:
        heapq.heappush(h, (-records[key], key))
    c = 0
    res = []
    while h and c < k:
        res.append(heapq.heappop(h)[1])
        c += 1
    return res


examples = [
    {
        "nums": [1, 1, 1, 2, 2, 3],
        "k": 2,
        "res": [1, 2]
    }, {
        "nums": [1],
        "k": 2,
        "res": [1, 2]
    }
]


for example in examples:
    print top_k_frequent(example["nums"], example["k"])
