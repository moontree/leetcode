"""
Median is the middle value in an ordered integer list.
 If the size of the list is even, there is no middle value.
 So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
For example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2
"""
import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.len = 0
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.left, -num)
        val = heapq.heappop(self.left)
        heapq.heappush(self.right, -val)
        if len(self.left) < len(self.right):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)

    def findMedian(self):
        """
        :rtype: float
        """
        # print self.left, self.right
        if len(self.left) == 0:
            return None
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        else:
            return -self.left[0]


obj = MedianFinder()
print obj.findMedian()

obj.addNum(6)
# print obj.findMedian()
obj.addNum(8)
print obj.findMedian()

obj.addNum(10)
print obj.findMedian()

obj.addNum(2)
print obj.findMedian()

obj.addNum(4)
print obj.findMedian()
