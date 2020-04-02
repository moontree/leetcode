"""
Given a set of non-overlapping intervals,
 insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""

examples = [
    {
        "intervals": [[1, 3], [6, 9]],
        "new_interval": [2, 5],
        "output": [[1, 5], [6, 9]]
    }, {
        "intervals": [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
        "new_interval": [4, 9],
        "output": [[1, 2], [3, 10], [12, 16]]
    }, {
        "intervals": [[1, 5]],
        "new_interval": [6, 9],
        "output": [[1, 5], [6, 9]]
    }, {
        "intervals": [[6, 9]],
        "new_interval": [1, 5],
        "output": [[1, 5], [6, 9]]
    }, {
        "intervals": [],
        "new_interval": [1, 5],
        "output": [[1, 5]]
    }, {
        "intervals": [[1, 9]],
        "new_interval": [1, 5],
        "output": [[1, 9]]
    }, {
        "intervals": [[1, 5]],
        "new_interval": [0, 1],
        "output": [[0, 5]]
    }
]


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def insert(intervals, newInterval):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    start_index = 0
    end_index = 0
    for i in range(len(intervals)):
        if intervals[i].end < newInterval.start:
            start_index += 1
        if intervals[i].start <= newInterval.end:
            end_index += 1
    if end_index < 1 or start_index > len(intervals) - 1:
        return intervals[:start_index] + [newInterval] + intervals[end_index:]
    else:
        merged_start = min(intervals[start_index].start, newInterval.start)
        merged_end = max(intervals[end_index - 1].end, newInterval.end)
        return intervals[:start_index] + [Interval(merged_start, merged_end)] + intervals[end_index:]


for example in examples:
    print '-------'
    inputs = []
    for p in example["intervals"]:
        inputs.append(Interval(p[0], p[1]))
    res = insert(inputs, Interval(example["new_interval"][0], example["new_interval"][1]))
    for p in res:
        print p.start, p.end
