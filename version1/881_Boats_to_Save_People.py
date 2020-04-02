"""
The i-th person has weight people[i],
and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time,
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
(It is guaranteed each person can be carried by a boat.)



Example 1:

Input:
    people = [1,2], limit = 3
Output:
    1
Explanation:
    1 boat (1, 2)

Example 2:

Input:
    people = [3,2,2,1], limit = 3
Output:
    3
Explanation:
    3 boats (1, 2), (2) and (3)

Example 3:

Input:
    people = [3,5,3,4], limit = 5
Output:
    4
Explanation:
    4 boats (3), (3), (4), (5)
Note:

    1 <= people.length <= 50000
    1 <= people[i] <= limit <= 30000

"""


class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        cnt = 0
        people.sort()
        l, r = 0, len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            cnt += 1
            r -= 1
        return cnt


examples = [
    {
        "input": {
            "people": [1, 2],
            "limit": 3,
        },
        "output": 1
    }, {
        "input": {
            "people": [3, 2, 2, 1],
            "limit": 3,
        },
        "output": 3
    }, {
        "input": {
            "people": [3, 5, 3, 4],
            "limit": 5,
        },
        "output": 4
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