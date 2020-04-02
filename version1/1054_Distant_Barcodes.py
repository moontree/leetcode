"""
In a warehouse, there is a row of barcodes,
where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.
You may return any answer, and it is guaranteed an answer exists.



Example 1:

Input:
    [1,1,1,2,2,2]
Output:
    [2,1,2,1,2,1]

Example 2:
Input:
    [1,1,1,1,2,2,3,3]
Output:
    [1,3,1,3,2,1,2,1]

Note:
    1 <= barcodes.length <= 10000
    1 <= barcodes[i] <= 10000
"""


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        cache = {}
        for v in barcodes:
            cache[v] = cache.get(v, 0) + 1
        nums = [[k, cache[k]] for k in cache]
        nums.sort(key=lambda x: -x[1])
        print(nums)
        res = [-1 for _ in range(len(barcodes))]
        i, j = 0, 1
        for v, c in nums:
            for _ in range(c):
                if i < len(barcodes):
                    res[i] = v
                    i += 2
                else:
                    res[j] = v
                    j += 2
        return res


examples = [
    {
        "input": {
            "barcodes": [1, 1, 1, 2, 2, 2],
        },
        "output": [2, 1, 2, 1, 2, 1]
    }, {
        "input": {
            "barcodes": [1, 1, 1, 1, 2, 2, 3, 3],
        },
        "output": [1, 3, 1, 3, 2, 1, 2, 1]
    }, {
        "input": {
            "barcodes": [2, 1, 1],
        },
        "output": [1, 2, 1]
    }, {
        "input": {
            "barcodes": [1, 1, 2],
        },
        "output": [1, 2, 1]
    }, {
        "input": {
            "barcodes": [2, 2, 1, 3],
        },
        "output": [2, 1, 2, 3]
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
