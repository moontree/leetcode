"""
Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
A scientist has index h if h of his/her N papers have at least h citations each,
 and the other N - h papers have no more than h citations each


For example, given citations = [3, 0, 6, 1, 5],
 which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
 Since the researcher has 3 papers with at least 3 citations each
  and the remaining two with no more than 3 citations each,
  his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

"""


def h_index(citations):
    """
    :type citations: List[int]
    :rtype: int
    """
    n = len(citations)
    counts = [0 for _ in range(n + 1)]
    for p in citations:
        if p > n:
            counts[n] += 1
        else:
            counts[p] += 1
    added = 0
    for i in range(n + 1)[::-1]:
        added += counts[i]
        if added >= i:
            return i


examples = [
    {
        "nums": [5, 5, 3],
        "res": 3
    }
]


for example in examples:
    print h_index(example["nums"])
