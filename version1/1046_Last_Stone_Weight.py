"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.
Return the weight of this stone (or 0 if there are no stones left.)



Example 1:

Input:
    [2,7,4,1,8,1]
Output:
    1
Explanation:
    We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
    we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
    we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
    we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

Note:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000
"""
import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        _stones = [-v for v in stones]
        heapq.heapify(_stones)
        while len(_stones) > 1:
            a = heapq.heappop(_stones)
            b = heapq.heappop(_stones)
            if a < b:
                heapq.heappush(_stones, a - b)
            print(-a, -b, _stones)
        print(_stones)
        if len(_stones) == 0:
            return 0
        return -_stones[0]


examples = [
    {
        "input": {
            "stones": [2, 7, 4, 1, 8, 1],
        },
        "output": 1
    }, {
        "input": {
            "stones": [2],
        },
        "output": 2
    }, {
        "input": {
            "stones": [2, 2],
        },
        "output": 0
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
