"""
On a table are N cards,
with a positive integer printed on the front and back of each card (possibly different).

We flip any number of cards, and after we choose one card.

If the number X on the back of the chosen card is not on the front of any card,
then this number X is good.

What is the smallest number that is good?
If no number is good, output 0.

Here, fronts[i] and backs[i] represent the number on the front and back of card i.

A flip swaps the front and back numbers,
so the value on the front is now on the back and vice versa.

Example:

Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is good.


Note:

1 <= fronts.length == backs.length <= 1000.
1 <= fronts[i] <= 2000.
1 <= backs[i] <= 2000.
"""


class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        n = len(fronts)
        cache = {}
        for i in range(n):
            if fronts[i] == backs[i]:
                cache[fronts[i]] = True
        rest = []
        for v in fronts:
            if v not in cache:
                rest.append(v)
        for v in backs:
            if v not in cache:
                rest.append(v)

        rest.sort()
        print rest
        return rest[0] if rest else 0


examples = [
    {
        "input": {
            "fronts": [1, 2, 4, 4, 7],
            "backs": [1, 3, 4, 1, 3],
        },
        "output": 2
    }, {
        "input": {
            "fronts": [1, 2, 2, 1, 7],
            "backs": [1, 3, 4, 2, 3],
        },
        "output": 2
    }, {
        "input": {
            "fronts": [1, 2, 4, 1, 3],
            "backs": [1, 2, 4, 2, 3],
        },
        "output": 0
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
        print func(**example['input']) == example['output']