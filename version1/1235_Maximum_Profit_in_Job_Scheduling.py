"""
We have n jobs,
where every job is scheduled to be done from startTime[i] to endTime[i],
obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays,
you need to output the maximum profit you can take such that
there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.


Example 1:

Input:
    startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output:
    120
Explanation:
    The subset chosen is the first and fourth job.
    Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Example 2:

Input:
    startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output:
    150
Explanation:
    The subset chosen is the first, fourth and fifth job.
    Profit obtained 150 = 20 + 70 + 60.

Example 3:

Input:
    startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output:
    6

Constraints:

    1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
    1 <= startTime[i] < endTime[i] <= 10^9
    1 <= profit[i] <= 10^4
"""
import bisect


class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        pairs = [[s, e, p] for s, e, p in zip(startTime, endTime, profit)]
        pairs.sort(key=lambda x: [x[1], x[0]])
        ends = []
        profits = []
        for s, e, p in pairs:
            idx = bisect.bisect_right(ends, s) - 1
            if idx == -1:
                if not ends:
                    profits.append(p)
                else:
                    profits.append(max(profits[-1], p))
                ends.append(e)
            else:
                if ends[-1] < e:
                    ends.append(e)
                    profits.append(max(profits[-1], profits[idx] + p))
                else:
                    profits[-1] = max(profits[-1],  profits[idx] + p)
        return profits[-1]


examples = [
    {
        "input": {
            "startTime": [1, 2, 3, 3],
            "endTime": [3, 4, 5, 6],
            "profit": [50, 10, 40, 70]
        },
        "output": 120
    },  {
        "input": {
            "startTime": [1, 2, 3, 4, 6],
            "endTime": [3, 5, 10, 6, 9],
            "profit": [20, 20, 100, 70, 60]
        },
        "output": 150
    },  {
        "input": {
            "startTime": [1, 1, 1],
            "endTime": [2, 3, 4],
            "profit": [5, 6, 4]
        },
        "output": 6
    },
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
