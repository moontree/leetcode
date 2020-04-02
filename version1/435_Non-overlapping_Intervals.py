"""
Given a collection of intervals,
find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""
"""
compare two intervals,
[s1, e1], [s2, e2], in which s2 >= s1
if e2 <= e1:
    delete interval 1, use interval 2 to replace
elif s2 < e1:
    delete interval 2
else:
    keep both
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def erase_overlap_intervals(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    intervals.sort(key=lambda x: x.start)
    count, end = 0, -float("inf")
    for seg in intervals:
        if seg.end < e:
            count += 1
            end = seg.end
        elif seg.start < e:
            count += 1
        else:
            end = seg.end
    return count


examples = [
    {
        "intervals": [[1, 2], [2, 3], [3, 4], [1, 3]],
        "res": 1
    }, {
        "intervals": [[1, 2], [1, 2], [1, 2]],
        "res": 2
    }, {
        "intervals": [[1, 2], [2, 3]],
        "res": 0
    }, {
        "intervals": [[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]],
        "res": 2
    }
]


for example in examples:
    input = []
    for s, e in example["intervals"]:
        input.append(Interval(s, e))
    print erase_overlap_intervals(input)
