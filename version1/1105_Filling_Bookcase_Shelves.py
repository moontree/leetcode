"""
We have a sequence of books:
    the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width),
then build another level of shelf of the bookcase so that the total height of the bookcase has increased by
the maximum height of the books we just put down.
We repeat this process until there are no more books to place.

Note again that at each step of the above process,
the order of the books we place is the same order as the given sequence of books.
For example, if we have an ordered list of 5 books,
we might place the first and second book onto the first shelf,
the third book on the second shelf,
and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf
can be after placing shelves in this manner.



Example 1:


Input:
    books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output:
    6
Explanation:
    The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
    Notice that book number 2 does not have to be on the first shelf.


Constraints:

    1 <= books.length <= 1000
    1 <= books[i][0] <= shelf_width <= 1000
    1 <= books[i][1] <= 1000
"""


class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        dp = [float('inf') for _ in range(len(books))]
        n = len(books)
        for i in range(n):
            w, h = books[i][0], books[i][1]
            if i == 0:
                dp[i] = h
            else:
                dp[i] = min(dp[i], dp[i - 1] + h)
            for j in range(i - 1, -1, -1):
                ww, hh = books[j]
                w = w + ww
                h = max(h, hh)
                if w > shelf_width:
                    break
                else:
                    if j == 0:
                        dp[i] = min(dp[i], h)
                    else:
                        dp[i] = min(dp[i], dp[j - 1] + h)
        return dp[-1]


examples = [
    {
        "input": {
            "books": [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]],
            "shelf_width": 4
        },
        "output": 6
    }, {
        "input": {
            "books": [[7,3],[8,7],[2,7],[2,5]],
            "shelf_width": 10
        },
        "output": 15
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
