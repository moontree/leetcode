# encoding: utf-8
"""
In an exam room,
there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room,
they must sit in the seat that maximizes the distance to the closest person.
If there are multiple such seats, they sit in the seat with the lowest number.
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions:
ExamRoom.seat() returning an int representing what seat the student sat in,
and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.
It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.



Example 1:

Input:
    ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output:
    [null,0,9,4,2,null,5]
Explanation:
    ExamRoom(10) -> null
    seat() -> 0, no one is in the room, then the student sits at seat number 0.
    seat() -> 9, the student sits at the last seat number 9.
    seat() -> 4, the student sits at the last seat number 4.
    seat() -> 2, the student sits at the last seat number 2.
    leave(4) -> null
    seat() -> 5, the student sits at the last seat number 5.
​​​​​​​

Note:

    1 <= N <= 10^9
    ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
    Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

"""


class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.cache = []
        self.n = N - 1

    def seat(self):
        """
        :rtype: int
        """
        if len(self.cache) == 0:
            self.cache.append(0)
            return 0
        else:
            l, d, xx = -1, 0, -1
            if self.cache[0] != 0:
                d, xx = self.cache[0], 0
            for i in range(len(self.cache) - 1):
                x = (self.cache[i] + self.cache[i + 1]) / 2
                if x - self.cache[i] > d:
                    l, d, xx = i, x - self.cache[i], x
            if self.cache[-1] != self.n:
                if self.n - self.cache[-1] > d:
                    l, xx = len(self.cache) - 1, self.n
            self.cache[l + 1: l + 1] = [xx]
            return xx

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        self.cache.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

if __name__ == '__main__':
    obj = ExamRoom(10)
    print obj.seat()
    print obj.seat()
    print obj.seat()
    print obj.seat()
    obj.leave(4)
    print obj.seat()
