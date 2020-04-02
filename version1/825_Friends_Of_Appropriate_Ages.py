"""
Some people will make friend requests.
The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

    age[B] <= 0.5 * age[A] + 7
    age[B] > age[A]
    age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.
Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input:
    [16,16]
Output:
    2
Explanation:
    2 people friend request each other.


Example 2:
Input:
    [16,17,18]
Output:
    2
Explanation:
    Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input:
    [20,30,100,110,120]
Output:
    3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

"""
import bisect


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        count = 0
        cache = {}
        for v in ages:
            if v not in cache:
                left = bisect.bisect_right(ages, 0.5 * v + 7)
                right = bisect.bisect_right(ages, v)
                cache[v] = max(right - left - 1, 0)
            count += cache[v]
        return count


examples = [
    {
        "input": {
            "ages": [16, 16],
        },
        "output": 2
    }, {
        "input": {
            "ages": [16, 17, 18]
        },
        "output": 2
    }, {
        "input": {
            "ages": [20, 30, 100, 110, 120],
        },
        "output": 3
    }, {
        "input": {
            "ages": [108, 115, 5, 24, 82],
        },
        "output": 3
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
        print v, v == example['output']