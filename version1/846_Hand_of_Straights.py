"""
Alice has a hand of cards,
given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W,
and consists of W consecutive cards.

Return true if and only if she can.



Example 1:

Input:
    hand = [1,2,3,6,2,3,4,7,8], W = 3
Output:
    true
Explanation:
    Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

Example 2:

Input:
    hand = [1,2,3,4,5], W = 4
Output:
    false
Explanation:
    Alice's hand can't be rearranged into groups of 4.


Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

"""


class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % W != 0:
            return False
        gn = len(hand) / W
        cache = {}
        for v in hand:
            cache[v] = cache.get(v, 0) + 1
        values = cache.keys()
        values.sort()
        s = 0
        for _ in range(gn):
            if s + W - 1 < len(values) and values[s + W - 1] - values[s] == W - 1:
                print s, values[s: s + W]
                find = False
                for i in range(s, s + W):
                    v = values[i]
                    cache[v] = cache.get(v) - 1
                    if cache[v] == -1:
                        return False
                    elif cache[v] == 0:
                        pass
                    else:
                        if not find:
                            find = True
                            s = i
                if not find:
                    s = s + W
            else:
                return False
        return True


examples = [
    {
        "input": {
            "hand": [1, 2, 3, 6, 2, 3, 4, 7, 8],
            "W": 3
        },
        "output": True
    }, {
        "input": {
            "hand": [1, 2, 3, 4, 5],
            "W": 4
        },
        "output": False
    }, {
        "input": {
            "hand": [1, 1, 2, 2, 3, 3],
            "W": 3
        },
        "output": True
    }, {
        "input": {
            "hand": [5, 1],
            "W": 1
        },
        "output": True
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
