"""
Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums,
there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
 Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].
"""
import bisect
import heapq


def median_sliding_window(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[float]
    """
    window = nums[:k]
    window.sort()
    res = []
    start = k / 2
    if k % 2 == 1:
        res.append(window[start] + 0.0)
    else:
        a, b = window[start - 1], window[start]
        res.append((a + b) / 2.0)
    for i in xrange(len(nums) - k):
        idx = bisect.bisect_left(window, nums[i])
        window.pop(idx)
        idx = bisect.bisect_left(window, nums[i + k])
        window.insert(idx, nums[i + k])
        if k % 2 == 1:
            res.append(window[start] + 0.0)
        else:
            a, b = window[start - 1], window[start]
            res.append((a + b) / 2.0)
    return res


def median_sliding_window_heap(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[float]
    """
    left, right = k / 2, k - k / 2
    res = []
    hl, hr = [], []
    for i, v in enumerate(nums[:k]):
        heapq.heappush(hr, (v, i))
    while len(hr) > right:
        heapq.heappush(hl, (-hr[0][0], hr[0][1]))
        heapq.heappop(hr)
    if k % 2 == 1:
        res.append(hr[0][0] + 0.0)
    else:
        res.append((hr[0][0] - hl[0][0]) / 2.0)
    for i in xrange(len(nums) - k):
        old_val, new_val = nums[i], nums[i + k]
        if new_val >= hr[0][0]:
            heapq.heappush(hr, (new_val, i + k))
            if hl and old_val <= -hl[0][0]:
                heapq.heappush(hl, (-hr[0][0], hr[0][1]))
                heapq.heappop(hr)
        else:
            heapq.heappush(hl, (-new_val, i + k))
            if hr and old_val >= hr[0][0]:
                heapq.heappush(hr, (-hl[0][0], hl[0][1]))
                heapq.heappop(hl)

        while hl and hl[0][1] <= i:
            heapq.heappop(hl)
        while hr and hr[0][1] <= i:
            heapq.heappop(hr)
        if k % 2 == 1:
            res.append(hr[0][0] + 0.0)
        else:
            res.append((hr[0][0] - hl[0][0]) / 2.0)

    return res


examples = [
    {
        "nums": [1, 3, -1, -3, 5, 3, 6, 7],
        "k": 3
    }, {
        "nums": [1, 3, -1, -3, 5, 3, 6, 7],
        "k": 2
    }, {
        "nums": [1, 3],
        "k": 1
    }, {
        "nums": [1, 4, 2, 3],
        "k": 4
    }
]


for example in examples:
    print median_sliding_window_heap(example["nums"], example["k"])
