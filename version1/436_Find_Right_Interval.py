"""
Given a set of intervals, for each of the interval i,
 check if there exists an interval j whose start point is bigger than or equal to the end point of the interval i,
 which can be called that j is on the "right" of i.

For any interval i, you need to store the minimum interval j's index,
which means that the interval j has the minimum start point to build the "right" relationship for interval i.
 If the interval j doesn't exist, store -1 for the interval i.
 Finally, you need output the stored value of each interval as an array.

Note:
You may assume the interval's end point is always bigger than its start point.
You may assume none of these intervals have the same start point.
Example 1:
Input: [ [1,2] ]

Output: [-1]

Explanation: There is only one interval in the collection, so it outputs -1.
Example 2:
Input: [ [3,4], [2,3], [1,2] ]

Output: [-1, 0, 1]

Explanation: There is no satisfied "right" interval for [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point;
For [1,2], the interval [2,3] has minimum-"right" start point.
Example 3:
Input: [ [1,4], [2,3], [3,4] ]

Output: [-1, 2, -1]

Explanation: There is no satisfied "right" interval for [1,4] and [3,4].
For [2,3], the interval [3,4] has minimum-"right" start point.
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def find_right_interval(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[int]
    """
    points = []
    for i, p in enumerate(intervals):
        points.append([p.start, 1, i])
        points.append([p.end, 0, i])
    points.sort()
    right = None
    res = [-1 for _ in xrange(len(intervals))]
    for v, flag, i in points[::-1]:
        if flag == 0 and right is not None:
            res[i] = right
        elif flag == 1:
            right = i
    return res


examples = [
    {
        "intervals": [[1, 2]],
        "res": [-1]
    }, {
        "intervals": [[3, 4], [2, 3], [1, 2]],
        "res": [-1, 0, 1]
    }, {
        "intervals": [[1, 4], [2, 3], [3, 4]],
        "res": [-1, 2, -1]
    }
]


for example in examples:
    input = []
    for s, e in example["intervals"]:
        input.append(Interval(s, e))
    print find_right_interval(input)