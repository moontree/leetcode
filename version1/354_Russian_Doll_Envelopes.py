"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of
one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).


"""
import bisect


def max_envelopes(envelopes):
    """
    :type envelopes: List[List[int]]
    :rtype: int
    """
    if not envelopes:
        return 0
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    """
    only one height will be choose when width is same
    """
    h = []
    for i, e in enumerate(envelopes, 0):
        # print i, e
        j = bisect.bisect_left(h, e[1])
        if j < len(h):
            h[j] = e[1]
        else:
            h.append(e[1])
    return len(h)


examples = [
    {
        "envelopes": [
            [2, 3], [2, 4], [3, 3],
        ],
        "res": 3
    }, {
        "envelopes": [
            [10, 8], [1, 12], [6, 15], [2, 18]
        ],
        "res": 3
    }
]


for example in examples:
    print max_envelopes(example["envelopes"])
