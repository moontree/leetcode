"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?


"""


def candy(ratings):
    """
    :type ratings: List[int]
    :rtype: int
    """
    nums = len(ratings)
    res = 0
    prev = 0
    down = 0
    height = 0
    for i in range(nums):
        if not i:
            res = prev = 1
        else:
            if ratings[i] < ratings[i - 1]:
                if not height:
                    height = prev
                down += 1
                prev = 1
            else:
                if ratings[i] > ratings[i - 1]:
                    prev += 1
                else:
                    prev = 1
                if down:
                    res += (down + 1) * down // 2 + max(down + 1 - height, 0)
                    down = height = 0
                res += prev
    if down:
        res += max(down + 1 - height, 0)
    res += (down + 1) * down // 2
    return res

    # while start < nums:
    #     if flag == -1 or flag == 1:
    #         start -= 1
    #     end = start + 1
    #     if end < nums and ratings[end] == ratings[end - 1]:
    #         flag = 0
    #     elif end < nums and ratings[end] > ratings[end - 1]:
    #         while end < nums and ratings[end] > ratings[end - 1]:
    #             end += 1
    #         for j in range(start + 1, end):
    #             left_increase[j] = j - start + 1
    #         flag = 1
    #     else:
    #         while end < nums and ratings[end] < ratings[end - 1]:
    #             end += 1
    #         if left_increase[start] < end - start:
    #             left_increase[start] = end - start
    #         for j in range(start + 1, end):
    #             left_increase[j] = end - j
    #         flag = -1
    #     start = end
    # return sum(left_increase)


examples = [
    {
        "ratings": [1, 1, 1],
        "res": 3
    }, {
        "ratings": [1, 2, 3],
        "res": 6
    }, {
        "ratings": [1, 2, 1],
        "res": 4
    }, {
        "ratings": [1, 2, 2],
        "res": 4
    }, {
        "ratings": [4, 3, 2, 4, 1, 4],
        "res": 11
    }, {
        "ratings": [4, 2, 3, 4, 1],
        "res": 9
    }, {
        "ratings": [2, 1],
        "res": 3
    }
]


for examle in examples:
    print candy(examle["ratings"])
