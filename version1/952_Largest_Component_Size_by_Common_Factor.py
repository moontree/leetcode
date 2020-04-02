"""
Given a non-empty array of unique positive integers A,
consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.



Example 1:
Input:
    [4 ,6, 15, 35]
Output:
    4

Example 2:
Input:
    [20,50,9,63]
Output:
    2

Example 3:
Input:
    [2,3,6,7,4,12,21,39]
Output:
    8

Note:
    1 <= A.length <= 20000
    1 <= A[i] <= 100000
"""


class DSU:
    def __init__(self, primes):
        self.p = {p: p for p in primes}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.p[xr] = yr


class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        B = []
        for n in A:
            d = 2
            facs = []
            while d * d <= n:
                if n % d == 0:
                    while n % d == 0:
                        n /= d
                    facs.append(d)
                d += 1

            if n > 1 or len(facs) == 0:
                facs.append(n)
            B.append(facs)

        primes = list({p for facs in B for p in facs})
        dsu = DSU(primes)
        for facs in B:
            for fac in facs:
                dsu.union(facs[0], fac)

        counts = {}
        for facs in B:
            v = dsu.find(facs[0])
            counts[v] = counts.get(v, 0) + 1

        return max(counts.values())


examples = [
    {
        "input": {
            "A": [4, 6, 15, 35],
        },
        "output": 4
    }, {
        "input": {
            "A": [20, 50, 9, 63],
        },
        "output": 2
    }, {
        "input": {
            "A": [2, 3, 6, 7, 4, 12, 21, 39],
        },
        "output": 8
    }, {
        "input": {
            "A": [98, 39, 14, 86, 56, 89, 26, 59, 63],
        },
        "output": 7
    }, {
        "input": {
            "A": [2,7,522,526,535,26,944,35,519,45,48,567,266,68,74,591,81,86,602,93,610,621,111,114,629,641,131,651,142,659,669,161,674,163,180,187,190,194,195,206,207,218,737,229,240,757,770,260,778,270,272,785,274,290,291,292,296,810,816,314,829,833,841,349,880,369,147,897,387,390,905,405,406,407,414,416,417,425,938,429,432,926,959,960,449,963,966,929,457,463,981,985,79,487,1000,494,508],
        },
        "output": 84
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
