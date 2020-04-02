"""
Today, the bookstore owner has a store open for customers.length minutes.
Every minute, some number of customers (customers[i]) enter the store,
and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.
If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.
When the bookstore owner is grumpy,
the customers of that minute are not satisfied,
otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight,
but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.



Example 1:

Input:
    customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output:
    16
Explanation:
    The bookstore owner keeps themselves not grumpy for the last 3 minutes.
    The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.


Note:

    1 <= X <= customers.length == grumpy.length <= 20000
    0 <= customers[i] <= 1000
    0 <= grumpy[i] <= 1
"""


class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        n = len(customers)
        base, more, max_val = 0, 0, 0
        q = []
        X -= 1
        for i in range(n):
            if grumpy[i]:
                if q and i - q[0][0] > X:
                    more -= q[0][1]
                    q.pop(0)
                more += customers[i]
                q.append([i, customers[i]])
                max_val = max(more, max_val)
            else:
                base += customers[i]

        return base + max_val


examples = [
    {
        "input": {
            "customers": [1, 0, 1, 2, 1, 1, 7, 5],
            "grumpy": [0, 1, 0, 1, 0, 1, 0, 1],
            "X": 3
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
