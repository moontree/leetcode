"""
In a row of trees,
the i-th tree produces fruit with type tree[i].

You start at any tree of your choice,
then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.
If you cannot, stop.

Move to the next tree to the right of the current tree.
If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree:
 you must perform step 1, then step 2, then back to step 1,
 then step 2, and so on until you stop.

You have two baskets,
and each basket can carry any quantity of fruit,
but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input:
    [1,2,1]
Output:
    3
Explanation:
    We can collect [1,2,1].

Example 2:

Input:
    [0,1,2,2]
Output:
    3
Explanation:
    We can collect [1,2,2].
    If we started at the first tree, we would only collect [0, 1].

Example 3:

Input:
    [1,2,3,2,2]
Output:
    4
Explanation:
    We can collect [2,3,2,2].
    If we started at the first tree, we would only collect [1, 2].

Example 4:

Input:
    [3,3,3,1,2,1,1,2,3,3,4]
Output:
    5
Explanation:
    We can collect [1,2,1,1,2].
    If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

    1 <= tree.length <= 40000
    0 <= tree[i] < tree.length

"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        q = []
        idx = []
        res = 0
        s = 0
        for i, v in enumerate(tree):
            if not q:
                q.append(v)
                idx.append(i)
            elif v == q[-1]:
                pass
            else:
                if len(q) == 1:
                    q.append(v)
                    idx.append(i)
                else: # len(q) == 2
                    if v == q[0]:
                        idx[0] = i
                        q = q[::-1]
                        idx = idx[::-1]
                    else:
                        q[0], q[1] = q[1], v
                        idx[0], idx[1] = idx[1], i
                        s = idx[0]
            tmp = i - s + 1
            if res < tmp:
                res = tmp
            # print (i, v, s, tree[s: i + 1], '---', q, idx)
        return res


examples = [
    {
        "input": {
            "tree": [1, 2, 1],
        },
        "output": 3
    }, {
        "input": {
            "tree": [0, 1, 2, 2],
        },
        "output": 3
    }, {
        "input": {
            "tree": [1, 2, 3, 2, 2],
        },
        "output": 4
    }, {
        "input": {
            "tree": [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4],
        },
        "output": 5
    }, {
        "input": {
            "tree": [0],
        },
        "output": 1
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
