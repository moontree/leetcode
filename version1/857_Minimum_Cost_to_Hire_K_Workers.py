"""
There are N workers.
The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.
When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.



Example 1:

Input:
    quality = [10,20,5], wage = [70,50,30], K = 2
Output:
    105.00000
Explanation:
    We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

Input:
    quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output:
    30.66667
Explanation:
    We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.

Note:
    1 <= K <= N <= 10000, where N = quality.length = wage.length
    1 <= quality[i] <= 10000
    1 <= wage[i] <= 10000
    Answers within 10^-5 of the correct answer will be considered correct.
"""
import heapq


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        n = len(quality)
        pairs = [[wage[i] * 1.0 / quality[i], quality[i]] for i in range(n)]
        pairs.sort()
        q = [-item[1] for item in pairs[:K]]
        heapq.heapify(q)
        total = -sum(q)
        total_cost = pairs[K - 1][0] * total
        for cost, weight in pairs[K:]:
            nw = total + q[0] + weight
            tmp_total_cost = cost * nw
            heapq.heappop(q)
            heapq.heappush(q, -weight)
            total = nw
            if tmp_total_cost <= total_cost:
                total_cost = tmp_total_cost

        return total_cost


examples = [
    {
        "input": {
            "quality": [10, 20, 5],
            "wage": [70, 50, 30],
            "K": 2
        },
        "output": 105.0
    }, {
        "input": {
            "quality": [3, 1, 10, 10, 1],
            "wage": [4, 8, 2, 2, 7],
            "K": 3
        },
        "output": 30.666667
    }, {
        "input": {
            "quality": [3, 1, 5, 10, 1],
            "wage": [4, 8, 1, 2, 7],
            "K": 3
        },
        "output": 24
    }, {
        "input": {
            "quality": [14, 56, 59, 89, 39, 26, 86, 76, 3, 36],
            "wage": [90, 217, 301, 202, 294, 445, 473, 245, 415, 487],
            "K": 2
        },
        "output": 399.53846
    }, {
        "input": {
            "quality": [1, 1, 1, 10, 10],
            "wage": [6, 7, 8, 1, 1],
            "K": 3
        },
        "output": 24.0
    }, {
        "input": {
            "quality": [32, 43, 66, 9, 94, 57, 25, 44, 99, 19],
            "wage": [187, 366, 117, 363, 121, 494, 348, 382, 385, 262],
            "K": 4
        },
        "output": 1528.0
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
        print v, abs(v - example['output']) < 0.00001
