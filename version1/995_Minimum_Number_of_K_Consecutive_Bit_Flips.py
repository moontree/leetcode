# --*-- encoding: utf-8 --*--
"""
In an array A containing only 0s and 1s,
a K-bit flip consists of choosing a (contiguous) subarray of length K and
simultaneously changing every 0 in the subarray to 1,
and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.
If it is not possible, return -1.


Example 1:

Input:
    A = [0,1,0], K = 1
Output:
    2
Explanation:
    Flip A[0], then flip A[2].

Example 2:

Input:
    A = [1,1,0], K = 2
Output:
    -1
Explanation:
    No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].

Example 3:

Input:
    A = [0,0,0,1,0,1,1,0], K = 3
Output:
    3
Explanation:
    Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
    Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
    Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

Note:
    1 <= A.length <= 30000
    1 <= K <= A.length
"""


class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        hint = [0] * N
        ans = flip = 0

        for i, x in enumerate(A):
            flip ^= hint[i]
            if x ^ flip == 0:
                ans += 1
                if i + K > N:
                    return -1
                flip ^= 1
                if i + K < N:
                    hint[i + K] ^= 1
        return ans

        # q = []
        # res = 0
        # for i in range(len(A)):
        #     while q and q[0] <= i - K:
        #         q.pop(0)
        #     if A[i] == len(q) % 2:
        #         res += 1
        #         q.append(i)
        #         if i + K > len(A):
        #             return -1
        # return res


        # i: left is i [i: i + K]
        # print(len(A))
        # s = [0]  # total flips before i, then, in k range, flip nums is S[i] - S[max(i - k + 1, 0)]
        # for i in range(len(A) - K + 1):
        #     flips = s[i] - s[max(i - K + 1, 0)]
        #     v = A[i] if flips % 2 == 0 else 1 - A[i]
        #     if v == 1:
        #         s.append(s[-1])
        #     else:
        #         s.append(s[-1] + 1)
        # for i in range(max(len(A) - K + 1, 0), len(A)):
        #     flips = s[-1] - s[max(i - K + 1, 0)]
        #     v = A[i] if flips % 2 == 0 else 1 - A[i]
        #     if v == 0:
        #         return -1
        # return s[-1]


examples = [
    {
        "input": {
            "A": [0, 1, 0],
            "K": 1
        },
        "output": 2
    }, {
        "input": {
            "A": [1, 1, 0],
            "K": 2
        },
        "output": -1
    }, {
        "input": {
            "A": [0, 0, 0, 1, 0, 1, 1, 0],
            "K": 3
        },
        "output": 3
    # }
    }, {
        "input": {
            "A": [1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,1,0,0,1,1,1,1,1,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,1,1,0,0,1,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,1,0,1,1,0,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,1,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,1,1,1,1,0,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,1,1,1,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,1,1,1,1,0,0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,1,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,1,1,0,1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,1,1,0,1,0,0,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,1,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,1,1,1,0,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,1,1,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,0,1,0,1,1,0,1,1,0,0,1],
            "K": 5000
        },
        "output": -1
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