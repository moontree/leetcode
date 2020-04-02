"""
Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order.
Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.



Example:

Input:
    tasks = ["A","A","A","B","B","B"], n = 2
Output:
    8
Explanation:
    A -> B -> idle -> A -> B -> idle -> A -> B.


Note:

    The number of tasks is in the range [1, 10000].
    The integer n is in the range [0, 100].
"""


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cache = {}
        for c in tasks:
            cache[c] = cache.get(c, 0) + 1
        pairs = [[k, v] for k, v in cache.items()]
        pairs.sort(key=lambda x: -x[1])

        cc = pairs[0][1]
        res = (cc - 1) * (n + 1)
        for k, v in pairs:
            if v == cc:
                res += 1
        return res if res > len(tasks) else len(tasks)


examples = [
    {
        "input": {
            "tasks": ["A", "A", "A", "B", "B", "B"],
            "n": 0
        },
        "output": 8
    }, {
        "input": {
            "tasks": ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"],
            "n": 2
        },
        "output": 16
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
