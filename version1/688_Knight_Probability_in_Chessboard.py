"""
On an NxN chessboard,
a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make,
as illustrated below. Each move is two squares in a cardinal direction,
then one square in an orthogonal direction.

 Each time the knight is to move,
  it chooses one of eight possible moves uniformly at random
   (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard.
 Return the probability that the knight remains on the board after it has stopped moving.
"""


class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        directions = [[-2, -1], [-2, 1], [2, 1], [2, -1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
        def valid(x, y):
            if 0 <= x < N and 0 <= y < N:
                return True
            return False

        cur = {
            (r, c): 1
        }

        for i in range(K):
            tmp = {}
            for key in cur:
                x, y = key
                p = cur[key]
                for direction in directions:
                    xx = x + direction[0]
                    yy = y + direction[1]

                    if valid(xx, yy):
                        pp = p * 1. / 8
                        tmp[(xx, yy)] = tmp.get((xx, yy), 0) + pp
            cur = tmp
        return sum(cur.values())


if __name__ == '__main__':
    solution = Solution()
    print solution.knightProbability(3, 2, 0, 0)
    print solution.knightProbability(1, 2, 0, 0)
