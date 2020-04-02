"""
Koko loves to eat bananas.
There are N piles of bananas, the i-th pile has piles[i] bananas.
The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.
Each hour, she chooses some pile of bananas, and eats K bananas from that pile.
If the pile has less than K bananas, she eats all of them instead,
and won't eat any more bananas during this hour.

Koko likes to eat slowly,
but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.



Example 1:

Input:
    piles = [3,6,7,11], H = 8
Output:
    4

Example 2:

Input:
    piles = [30,11,23,4,20], H = 5
Output:
    30

Example 3:

Input:
    piles = [30,11,23,4,20], H = 6
Output:
    23

Note:

    1 <= piles.length <= 10^4
    piles.length <= H <= 10^9
    1 <= piles[i] <= 10^9
"""
import heapq
import math

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        speed = int(sum(piles) * 1.0 / H)
        if speed == 0:
            return 1
        while True:
            h = [math.ceil(p * 1.0 / speed) for p in piles]
            if sum(h) <= H:
                break
            else:
                speed += 1
        return speed


examples = [
    {
        "input": {
            "piles": [3, 6, 7, 11],
            "H": 8
        },
        "output": 4
    }, {
        "input": {
            "piles": [30, 11, 23, 4, 20],
            "H": 5
        },
        "output": 30
    }, {
        "input": {
            "piles": [30, 11, 23, 4, 20],
            "H": 6
        },
        "output": 23
    }, {
        "input": {
            "piles": [332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589,
                      290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184],
            "H": 823855818
        },
        "output": 14
    }, {
        "input": {
            "piles": [764170530, 60924085, 623419131, 41470026, 167201846, 855738664, 423577524, 3573329, 758308902, 984035489, 184594991, 619810993, 569362250, 32422497, 534913807, 555374151, 3559001, 931066259, 37998295, 84636025, 815148110, 192056541, 919062199],
            "H": 288303840
        },
        "output": 36
    }, {
        "input": {
            "piles": [312884470],
            "H": 968709470
        },
        "output": 1
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']
