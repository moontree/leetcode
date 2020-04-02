"""
Given two integers tomatoSlices and cheeseSlices.
The ingredients of different burgers are as follows:

    Jumbo Burger: 4 tomato slices and 1 cheese slice.
    Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small]
so that the number of remaining tomatoSlices equal to 0
and the number of remaining cheeseSlices equal to 0.
If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].


Example 1:

Input:
    tomatoSlices = 16, cheeseSlices = 7
Output:
    [1,6]
Explantion:
    To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
    There will be no remaining ingredients.

Example 2:

Input:
    tomatoSlices = 17, cheeseSlices = 4
Output:
    []
Explantion:
    There will be no way to use all ingredients to make small and jumbo burgers.

Example 3:

Input:
    tomatoSlices = 4, cheeseSlices = 17
Output:
    []
Explantion:
    Making 1 jumbo burger there will be 16 cheese remaining and
    making 2 small burgers there will be 15 cheese remaining.

Example 4:

Input:
    tomatoSlices = 0, cheeseSlices = 0
Output:
    [0,0]

Example 5:

Input:
    tomatoSlices = 2, cheeseSlices = 1
Output:
    [0,1]


Constraints:

    0 <= tomatoSlices <= 10^7
    0 <= cheeseSlices <= 10^7
"""


class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        a = tomatoSlices - cheeseSlices * 2
        if a < 0 or a % 2 == 1:
            return []
        x, y = a / 2, cheeseSlices - a / 2
        if y < 0:
            return []
        return [x, y]


examples = [
    {
        "input": {
            "tomatoSlices": 16,
            "cheeseSlices": 7
        },
        "output": [1, 6]
    }, {
        "input": {
            "tomatoSlices": 17,
            "cheeseSlices": 4
        },
        "output": []
    }, {
        "input": {
            "tomatoSlices": 4,
            "cheeseSlices": 17
        },
        "output": []
    }, {
        "input": {
            "tomatoSlices": 0,
            "cheeseSlices": 0
        },
        "output": [0, 0]
    }, {
        "input": {
            "tomatoSlices": 2,
            "cheeseSlices": 1
        },
        "output": [0, 1]
    }, {
        "input": {
            "tomatoSlices": 2385088,
            "cheeseSlices": 164763
        },
        "output": []
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
