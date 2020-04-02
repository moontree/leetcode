"""
Given an array A of strings,
find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.


Example 1:

Input:
    ["alex","loves","leetcode"]
Output:
    "alexlovesleetcode"

Explanation:
    All permutations of "alex","loves","leetcode" would also be accepted.

Example 2:

Input:
    ["catg","ctaagt","gcta","ttca","atgcatc"]
Output:
    "gctaagttcatgcatc"


Note:

    1 <= A.length <= 12
    1 <= A[i].length <= 20

"""
from heapq import heappush, heappop


class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        def concat(i, j):
            """
            Concatenate two words at given indices and return the length of the
            shared substring. The results are cached for reuse.
            """
            a, b = A[i], A[j]
            for r in range(len(b) - 1, -1, -1):
                if a.endswith(b[:r]):
                    return r
            return 0

        n = len(A)
        # mask the state wherein all the words are included
        end = (1 << n) - 1
        # a visit set to avoid cycles
        visited = set()

        # add an empty string to the min heap first as the kickstart for the
        # exhaustive search for the shortest path. The heap uses the length of
        # the concatenated string as the key.
        heap = [(0, '', 0, -1, -1)]
        while heap:
            length, ss, state, head, tail = heappop(heap)

            if state == end:
                return ss

            # cycle detection and avoidance
            if state in visited:
                continue
            visited.add(state)

            for i, s in enumerate(A):
                # check if the word has been included
                if state & (1 << i):
                    continue
                # set the bit for current index as the next state
                next_state = state | (1 << i)
                if head == -1:
                    heappush(heap, (len(s), s, next_state, i, i))
                else:
                    # the word can be concatenated in both ends, resulting
                    # different concatenations
                    a, b = concat(tail, i), concat(i, head)
                    # concate the strings properly
                    sa, sb = ss + (s[a:] if a else s), (s[:len(s) - b] if b else s) + ss
                    # move to next step
                    heappush(heap, (len(sa), sa, next_state, head, i))
                    heappush(heap, (len(sb), sb, next_state, i, tail))



examples = [
    {
        "input": {
            "A": ["alex", "loves", "leetcode"],
        },
        "output": "alexlovesleetcode"
    }, {
        "input": {
            "A": ["catg", "ctaagt", "gcta", "ttca", "atgcatc"],
        },
        "output": "gctaagttcatgcatc"
    }, {
        "input": {
            "A": ["fkwel", "pbcba", "kpbc", "bcbab", "pfkwe"],
        },
        "output": "kpbcbabpfkwel"
    }
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
