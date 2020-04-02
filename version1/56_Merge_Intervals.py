"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]
"""

examples = [
    {
        "intervals": [[1, 3], [2, 6], [8, 10], [15, 18]],
        "output": [[1, 6], [8, 10], [15, 18]]
    }, {
        "intervals": [[1, 3], [2, 6], [8, 10], [5, 18]],
        "output": [[1, 18]]
    }
]


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    res = []
    if len(intervals):
        intervals.sort(key=lambda s: s.start)
        l = intervals[0].start
        r = intervals[0].end
        for pair in intervals:
            if pair.start <= r:
                if r < pair.end:
                    r = pair.end
            else:
                res.append(Interval(l, r))
                l = pair.start
                r = pair.end
        res.append(Interval(l, r))
    return res


for example in examples:
    inputs = []
    for p in example["intervals"]:
        inputs.append(Interval(p[0], p[1]))
    print merge(inputs)
