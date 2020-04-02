"""
=========================
Project -> File: leetcode -> 1386_Cinema_Seat_Allocation.py
Author: zhangchao
=========================
A cinema has n rows of seats,
numbered from 1 to n and there are ten seats in each row,
labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved,
for example, reservedSeats[i]=[3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person families you can allocate on the cinema seats.
A four-person family occupies fours seats in one row, that are next to each other.
Seats across an aisle (such as [3,3] and [3,4]) are not considered to be next to each other,
however,
It is permissible for the four-person family to be separated by an aisle,
but in that case, exactly two people have to sit on each side of the aisle.

Example 1:

Input:
    n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output:
    4
Explanation:
    The figure above shows the optimal allocation for four families,
    where seats mark with blue are already reserved and contiguous seats mark with orange are for one family.

Example 2:

Input:
    n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output:
    2

Example 3:

Input:
    n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output:
    4

Constraints:
    1 <= n <= 10^9
    1 <= reservedSeats.length <= min(10*n, 10^4)
    reservedSeats[i].length == 2
    1 <= reservedSeats[i][0] <= n
    1 <= reservedSeats[i][1] <= 10
    All reservedSeats[i] are distinct.
"""


class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reachable = [15 << 1, 15 << 5, 15 << 3, 255 << 1]
        cache = {}
        for r, c in reservedSeats:
            cache[r] = cache.get(r, 0) + (1 << (c - 1))
        res = 0
        for v in cache.values():
            if v & reachable[-1] == 0:
                res += 2
            elif v & reachable[0] == 0 or v & reachable[1] == 0 or v & reachable[2] == 0:
                res += 1
        res += 2 * (n - len(cache))
        return res


examples = [
    {
        "input": {
            "n": 3,
            "reservedSeats": [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
        },
        "output": 4
    }, {
        "input": {
            "n": 2,
            "reservedSeats": [[2, 1], [1, 8], [2, 6]]
        },
        "output": 2
    }, {
        "input": {
            "n": 4,
            "reservedSeats": [[4, 3], [1, 4], [4, 6], [1, 7]]
        },
        "output": 4
    }
]

import time

if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
