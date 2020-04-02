"""
=========================
Project -> File: leetcode -> 1333_Filter_Restaurants_by_Vegan_Friendly_Price_and_Distance.py
Author: zhangchao
=========================
Given the array restaurants where
restaurants[i] = [id_i, rating_i, veganFriendly_i, price_i, distance_i].
You have to filter the restaurants using three filters.

The veganFriendly filter will be either true
(meaning you should only include restaurants with veganFriendlyi set to true)
or false (meaning you can include any restaurant).
In addition, you have the filters maxPrice and maxDistance
which are the maximum value for price and distance of restaurants you should consider respectively.

Return the array of restaurant IDs after filtering,
ordered by rating from highest to lowest.
For restaurants with the same rating,
order them by id from highest to lowest.
For simplicity veganFriendly_i and veganFriendly take value 1 when it is true, and 0 when it is false.



Example 1:

Input:
    restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
    veganFriendly = 1, maxPrice = 50, maxDistance = 10
Output:
    [3,1,5]
Explanation:
    The restaurants are:
    Restaurant 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
    Restaurant 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
    Restaurant 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
    Restaurant 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
    Restaurant 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1]
    After filter restaurants with veganFriendly = 1, maxPrice = 50 and maxDistance = 10
    we have restaurant 3, restaurant 1 and restaurant 5 (ordered by rating from highest to lowest).

Example 2:

Input:
    restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
    veganFriendly = 0, maxPrice = 50, maxDistance = 10
Output:
    [4,3,2,1,5]
Explanation:
    The restaurants are the same as in example 1,
    but in this case the filter veganFriendly = 0,
    therefore all restaurants are considered.

Example 3:

Input:
    restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]],
    veganFriendly = 0, maxPrice = 30, maxDistance = 3
Output:
    [4,5]


Constraints:

    1 <= restaurants.length <= 10^4
    restaurants[i].length == 5
    1 <= idi, ratingi, pricei, distancei <= 10^5
    1 <= maxPrice, maxDistance <= 10^5
    veganFriendlyi and veganFriendly are 0 or 1.
    All id_i are distinct.
"""


class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        if veganFriendly:
            res = [item for item in restaurants if item[-2] <= maxPrice and item[-1] <= maxDistance and item[2]]
        else:
            res = [item for item in restaurants if item[-2] <= maxPrice and item[-1] <= maxDistance]
        res.sort(key=lambda x: [-x[1], -x[0]])
        return [x[0] for x in res]


examples = [
    {
        "input": {
            "restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
            "veganFriendly": 1,
            "maxPrice": 50,
            "maxDistance": 10,
        },
        "output": [3, 1, 5]
    }, {
        "input": {
            "restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
            "veganFriendly": 0,
            "maxPrice": 50,
            "maxDistance": 10,
        },
        "output": [4, 3, 2, 1, 5]
    }, {
        "input": {
            "restaurants": [[1, 4, 1, 40, 10], [2, 8, 0, 50, 5], [3, 8, 1, 30, 4], [4, 10, 0, 10, 3], [5, 1, 1, 15, 1]],
            "veganFriendly": 0,
            "maxPrice": 30,
            "maxDistance": 3,
        },
        "output": [4, 5]
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
