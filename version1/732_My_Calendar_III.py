"""
=========================
Project -> File: leetcode -> 732_My_Calendar_III.py
Author: zhangchao
=========================
Implement a MyCalendarThree class to store your events.
A new event can always be added.

Your class will have one method,
book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection
(ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book,
return an integer K representing the largest integer such that there exists a K-booking in the calendar.

Your class will be called like this:
MyCalendarThree cal = new MyCalendarThree();
MyCalendarThree.book(start, end)

Example 1:
    MyCalendarThree();
    MyCalendarThree.book(10, 20); // returns 1
    MyCalendarThree.book(50, 60); // returns 1
    MyCalendarThree.book(10, 40); // returns 2
    MyCalendarThree.book(5, 15); // returns 3
    MyCalendarThree.book(5, 10); // returns 3
    MyCalendarThree.book(25, 55); // returns 3
Explanation:
    The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
    The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
    The remaining events cause the maximum K-booking to be only a 3-booking.
    Note that the last event locally causes a 2-booking, but the answer is still 3 because
    eg. [10, 20), [10, 40), and [5, 15) are still triple booked.

Note:

    The number of calls to MyCalendarThree.book per test case will be at most 400.
    In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].

"""
import bisect


class MyCalendarThree(object):

    def __init__(self):
        self.pos = []
        self.delta = {}
        self.max = 0

    def book(self, start, end):
        i = bisect.bisect_left(self.pos, start)
        if start not in self.delta:
            self.delta[start] = self.delta[self.pos[i - 1]] if i else 0
            self.pos[i:i] = [start]

        j = bisect.bisect_left(self.pos, end)
        if end not in self.delta:
            self.delta[end] = self.delta[self.pos[j - 1]]
            self.pos[j:j] = [end]
        for k in range(i, j):
            self.delta[self.pos[k]] = c = self.delta[self.pos[k]] + 1
            self.max = max(self.max, c)
        return self.max


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

examples = [
    {
        "input": {
            "books": [
                [10, 20],
                [50, 60],
                [10, 40],
                [5, 15],
                [5, 10],
                [25, 55]
            ]
        },
        "output": [1, 1, 2, 3, 3, 3]
    }
]

import time


if __name__ == '__main__':

    for example in examples:
        obj = MyCalendarThree()
        print '----------'
        for (s, e), output in zip(example['input']['books'], example['output']):
            v = obj.book(s, e)
            print (s, e), v, v == output