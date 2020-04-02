"""
Given two words word1 and word2,
find the minimum number of steps required to convert word1 to word2.
(each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""


def min_distance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)
    distances = [[i for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        distances[i][0] = i
        for j in range(1, n + 1):
            distance_i_1_j_1 = distances[i - 1][j - 1]
            distance_i_j_1 = distances[i][j - 1]
            distance_i_1_j = distances[i - 1][j]
            if word1[i - 1] == word2[j - 1]:
                distance_i_1_j_1 -= 1
            distances[i][j] = min(distance_i_1_j_1, distance_i_1_j, distance_i_j_1) + 1
    return distances[-1][-1]


examples = [
    {
        "word1": "abc",
        "word2": "a",
        "distance": 2
    }, {
        "word1": "abc",
        "word2": "",
        "distance": 3
    }, {
        "word1": "ab",
        "word2": "bbafaf",
        "distance": 5
    }, {
        "word1": "",
        "word2": "",
        "distance": 0
    }
]


for example in examples:
    print min_distance(example["word1"], example["word2"])
