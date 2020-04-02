"""
Given two sequences pushed and popped with distinct values,
return true if and only if
this could have been the result of a sequence of push and pop operations on an initially empty stack.



Example 1:

Input:
    pushed = [1,2,3,4,5],
    popped = [4,5,3,2,1]
Output:
    true
Explanation:
    We might do the following sequence:
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input:
    pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output:
    false
Explanation:
    1 cannot be popped before 2.


Note:

    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed is a permutation of popped.
    pushed and popped have distinct values.
"""


class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        q = []
        i, j, n = 0, 0, len(pushed)
        for v in pushed:
            while q and j < n and q[-1] == popped[j]:
                q.pop()
                j += 1
            q.append(v)
        while q and j < n and q[-1] == popped[j]:
            q.pop()
            j += 1
        if j != n:
            return False
        return True


examples = [
    {
        "input": {
            "pushed": [1, 2, 3, 4, 5],
            "popped": [4, 5, 3, 2, 1],
        },
        "output": True
    }, {
        "input": {
            "pushed": [1, 2, 3, 4, 5],
            "popped": [4, 3, 5, 1, 2],
        },
        "output": False
    }, {
        "input": {
            "pushed": [1, 2, 3, 4, 5],
            "popped": [1, 2, 3, 4, 5],
        },
        "output": True
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
