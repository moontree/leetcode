"""
Given an array A, we may rotate it by a non-negative integer K so that the array becomes
A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].
Afterward, any entries that are less than or equal to their index are worth 1 point.

For example, if we have [2, 4, 1, 3, 0],
and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].
This is worth 3 points because
1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].

Over all possible rotations,
return the rotation index K that corresponds to the highest score we could receive.
If there are multiple answers, return the smallest such index K.

Example 1:
Input:
    [2, 3, 1, 4, 0]
Output:
    3
Explanation:
    Scores for each K are listed below:
    K = 0,  A = [2,3,1,4,0],    score 2
    K = 1,  A = [3,1,4,0,2],    score 3
    K = 2,  A = [1,4,0,2,3],    score 3
    K = 3,  A = [4,0,2,3,1],    score 4
    K = 4,  A = [0,2,3,1,4],    score 3
    So we should choose K = 3, which has the highest score.


Example 2:
Input: [1, 3, 0, 2, 4]
Output: 0
Explanation:  A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.
Note:

A will have length at most 20000.
A[i] will be in the range [0, A.length].
"""
import numpy as np


class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        adds = [0 for _ in range(n)]
        for i, v in enumerate(A):
            if i >= v:
                adds[0] += 1
                if i + 1 < n:
                    adds[i + 1] += 1
                ii = i - v + 1
                if ii < n:
                    adds[ii] += -1
                # adds[i + 1: n] += 1
                # adds[: i - v + 1] += 1

            else:
                adds[i + 1] += 1
                ii = n + i - v + 1
                if ii < n:
                    adds[ii] += -1
                # adds[i + 1: n + i - v + 1] += 1
        idx, v = 0, adds[0]
        for i in range(1, n):
            adds[i] += adds[i - 1]
            if v < adds[i]:
                v = adds[i]
                idx = i
        return idx


examples = [
    {
        "input": {
            "A": [2, 3, 1, 4, 0]
        },
        "output": 3
    }, {
        "input": {
            "A": [1, 3, 0, 2, 4]
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


"""
Example:
A: [2, 3, 1, 4, 0]
Range for 2: [1, 3] (Rotating the array for any value of 1 <= K <= 3 will give us a point for 2.
Range for 3: [2, 3]
Range for 1: [0, 1] and [3, 4]
... and so on

After doing that, 
the value of K that gives the highest score is the value that is common to the most # of ranges. 
The question is how do we solve for that value? 
A simple approach would be to keep an array, called count, 
with indices from 0 to 4, and add 1 to each indice for every range that contains it.
At the end the best value of k is the indice for which count has the largest value.

Example:
count would look like this if we added + 1 for range [1, 3]: 
count [0, 1, 1, 1, 0]. We would continue to add for every range. 
So after adding range [2, 3], count would look like [0, 1, 2, 2, 0] ... and so on.

But this would be O(n^2). We can improve this by making a simple adaptation. 
To represent some range [a, b] we can instead add +1 to only the indice a, 
and subtract 1 to the last b + 1 (if it exists). This would mean that we add +1 to every index >= a, 
and subtract -1 to every index b + 1. 
After doing this for every range,
we can accumate from the front, 
we should get the same array count, 
as we did with out n^2 version.
"""