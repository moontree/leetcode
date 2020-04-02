"""
We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:
    |S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.

Return the largest possible sum of the subset S.



Example 1:

Input:
    values = [5,4,3,2,1],
    labels = [1,1,2,2,3],
    num_wanted = 3,
    use_limit = 1
Output:
    9
Explanation:
    The subset chosen is the first, third, and fifth item.

Example 2:

Input:
    values = [5,4,3,2,1],
    labels = [1,3,3,3,2],
    num_wanted = 3,
    use_limit = 2

Output:
    12
Explanation:
    The subset chosen is the first, second, and third item.

Example 3:

Input:
    values = [9,8,8,7,6],
    labels = [0,0,0,1,1],
    num_wanted = 3,
    use_limit = 1
Output:
    16
Explanation:
    The subset chosen is the first and fourth item.

Example 4:
Input:
    values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output:
    24
Explanation:
    The subset chosen is the first, second, and fourth item.

Note:

    1 <= values.length == labels.length <= 20000
    0 <= values[i], labels[i] <= 20000
    1 <= num_wanted, use_limit <= values.length
"""


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        res = 0
        cache = {}
        pairs = [[value, label] for value, label in zip(values, labels)]
        pairs.sort(key=lambda x: -x[0])
        c = 0
        for v, l in pairs:
            if c == num_wanted:
                break
            if cache.get(l, 0) < use_limit:
                cache[l] = cache.get(l, 0) + 1
                res += v
                c += 1
        return res


examples = [
    {
        "input": {
            "values": [5, 4, 3, 2, 1],
            "labels": [1, 1, 2, 2, 3],
            "num_wanted": 3,
            "use_limit": 1,
        },
        "output": 9
    }, {
        "input": {
            "values": [5, 4, 3, 2, 1],
            "labels": [1, 3, 3, 3, 2],
            "num_wanted": 3,
            "use_limit": 2,
        },
        "output": 12
    }, {
        "input": {
            "values": [9, 8, 8, 7, 6],
            "labels": [0, 0, 0, 1, 1],
            "num_wanted": 3,
            "use_limit": 1,
        },
        "output": 16
    }, {
        "input": {
            "values": [9, 8, 8, 7, 6],
            "labels": [0, 0, 0, 1, 1],
            "num_wanted": 3,
            "use_limit": 2,
        },
        "output": 24
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
