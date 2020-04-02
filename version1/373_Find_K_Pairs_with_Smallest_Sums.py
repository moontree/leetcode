"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Given nums1 = [1,7,11], nums2 = [2,4,6],  k = 3

Return: [1,2],[1,4],[1,6]

The first 3 pairs are returned from the sequence:
[1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]


Example 2:
Given nums1 = [1,1,2], nums2 = [1,2,3],  k = 2

Return: [1,1],[1,1]

The first 2 pairs are returned from the sequence:
[1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:
Given nums1 = [1,2], nums2 = [3],  k = 3

Return: [1,3],[2,3]

All possible pairs are returned from the sequence:
[1,3],[2,3]
"""
import heapq


def k_smallest_pairs(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    # O(k * log(m))
    m, n = len(nums1), len(nums2)
    if m == 0 or n == 0:
        return []
    res = []
    window = []
    heapq.heappush(window, (nums1[0] + nums2[0], [0, 0]))
    for _ in xrange(k):
        if len(window):
            _, [r, c] = heapq.heappop(window)
            res.append([nums1[r], nums2[c]])
            if c == 0 and r + 1 < m:
                heapq.heappush(window, (nums1[r + 1] + nums2[0], [r + 1, 0]))
            if c + 1 < n:
                heapq.heappush(window, (nums1[r] + nums2[c + 1], [r, c + 1]))
        else:
            break
    return res


def k_smallest_pairs_using_sort(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[List[int]]
    """
    # mnlog(mn)
    sums = [[a + b, [a, b]] for b in nums2 for a in nums1]
    sums = sorted(sums, key = lambda x: x[0])
    res = [item[1] for item in sums[:k]]
    return res


examples = [
    {
        "input": {
            "nums1": [1, 7, 11],
            "nums2": [2, 4, 6],
            "k": 3
        },
        "output": [[1, 2], [1, 4], [1, 6]]
    }, {
        "input": {
            "nums1": [1, 1, 2],
            "nums2": [1, 2, 3],
            "k": 2
        },
        "output": [[1, 1], [1, 1]]
    }, {
        "input": {
            "nums1": [1, 2],
            "nums2": [3],
            "k": 3
        },
        "output": [[1, 3], [2, 3]]
    }, {
        "input": {
            "nums1": [1, 1, 2],
            "nums2": [1, 2, 3],
            "k": 10
        },
        "output": [[1]]
    }, {
        "input": {
            "nums1": [],
            "nums2": [1, 2, 3],
            "k": 10
        },
        "output": []
    }
]


for example in examples:
    print "------"
    print k_smallest_pairs(**example["input"])
