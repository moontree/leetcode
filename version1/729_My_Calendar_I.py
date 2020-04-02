"""
Implement a MyCalendar class to store your events.
A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end).
Formally, this represents a booking on the half open interval [start, end),
the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection
(ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book,
return true if the event can be added to the calendar successfully without causing a double booking.
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

"""


import bisect


class MyCalendar(object):

    def __init__(self):
        self.books = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        i1 = bisect.bisect_right(self.books, start)
        i2 = bisect.bisect_left(self.books, end)
        if i1 == i2 and i1 % 2 == 0:
            self.books.insert(i1, start)
            self.books.insert(i1 + 1, end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


examples = [
    {
        "input": [
            [10, 20],
            [15, 20],
            [20, 25]
        ],
        "output": [True, False, True]
    }
]


if __name__ == '__main__':

    for example in examples:
        obj = MyCalendar()
        print '----------'
        for (s, e), output in zip(example['input'], example['output']):
            print obj.book(s, e) == output