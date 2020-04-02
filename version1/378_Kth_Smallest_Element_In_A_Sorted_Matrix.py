"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
 find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

"""
import heapq
import bisect


def kth_smallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo < hi:
        mid = (lo + hi) // 2
        if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo
    # m, n = len(matrix), len(matrix[0])
    # h = []
    # heapq.heappush(h, (matrix[0][0], [0, 0]))
    # val = 0
    # for i in xrange(k):
    #     val, [r, c] = heapq.heappop(h)
    #     if c == 0 and r + 1 < m:
    #         heapq.heappush(h, (matrix[r + 1][0], [r + 1, 0]))
    #     if c + 1 < n:
    #         heapq.heappush(h, (matrix[r][c + 1], [r, c + 1]))
    # return val


examples = [
    {
        "input": {
            "matrix": [
                [ 1,  5,  9],
                [10, 11, 13],
                [12, 13, 15]
            ],
            "k": 8
        },
        "output": 13
    }
]


for example in examples:
    print kth_smallest(**example["input"])
