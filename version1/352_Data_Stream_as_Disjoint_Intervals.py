"""
Given a data stream input of non-negative integers a1, a2, ..., an, ...,
summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
"""
import heapq


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        heapq.heappush(self.intervals, (val, Interval(val, val)))

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        stack = []
        while self.intervals:
            start, cur = heapq.heappop(self.intervals)
            if not stack:
                stack.append((start, cur))
            else:
                _, prev = stack[-1]
                if cur.start <= prev.end + 1:
                    prev.end = max(prev.end, cur.end)
                else:
                    stack.append((start, cur))
        self.intervals = stack
        # return [[x[1].start, x[1].end] for x in self.intervals]
        return [x[1] for x in self.intervals]


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(1)
print obj.getIntervals()
obj.addNum(3)
print obj.getIntervals()

obj.addNum(7)
print obj.getIntervals()

obj.addNum(2)
print obj.getIntervals()

obj.addNum(6)
print obj.getIntervals()
