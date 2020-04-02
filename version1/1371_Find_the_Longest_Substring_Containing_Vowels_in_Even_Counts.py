"""
=========================
Project -> File: leetcode -> 1371_Find_the_Longest_Substring_Containing_Vowels_in_Even_Counts.py
Author: zhangchao
=========================
Given the string s,
return the size of the longest substring containing each vowel an even number of times.
That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.

Example 1:

Input:
    s = "eleetminicoworoep"
Output:
    13
Explanation:
    The longest substring is "leetminicowor"
     which contains two each of the vowels: e, i and o and zero of the vowels: a and u.

Example 2:

Input:
    s = "leetcodeisgreat"
Output:
    5
Explanation:
    The longest substring is "leetc" which contains two e's.

Example 3:

Input:
    s = "bcbcbc"
Output:
    6
Explanation:
    In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.


Constraints:

    1 <= s.length <= 5 x 10^5
    s contains only lowercase English letters.
"""


class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = {c: 1 << i for i, c in enumerate('aeiou')}
        pos = {0: -1}
        res = 0
        status = 0
        for i, c in enumerate(s):
            if c in cache:
                status ^= cache[c]
            if status in pos:
                res = max(i - pos[status], res)
            else:
                pos[status] = i
        return res


examples = [
    {
        "input": {
            "s": "eleetminicoworoep",
        },
        "output": 13
    }, {
        "input": {
            "s": "leetcodeisgreat",
        },
        "output": 5
    }, {
        "input": {
            "s": "bcbcbc",
        },
        "output": 6
    }
    , {
        "input": {
            "s": "tyrwpvlifrgjghlcicyocusukhmjbkfkzsjhkdrtsztchhazhmcircxcauajyzlppedqyzkcqvffyeekjdwqtjegerxbyktzvrxwgfjnrfbwvhiycvoznriroroamkfipazunsabwlseseeiimsmftchpafqkquovuxhhkpvphwnkrtxuiuhbcyqulfqyzgjjwjrlfwwxotcdtqsmfeingsxyzbpvmwulmqfrxbqcziudixceytvvwcohmznmfkoetpgdntrndvjihmxragqosaauthigfjergijsyivozzfrlpndygsmgjzdzadsxarjvyxuecqlszjnqvlyqkadowoljrmkzxvspdummgraiutxxxqgotqnxwjwfotvqglqavmsnmktsxwxcpxhuujuanxueuymzifycytalizwnvrjeoipfoqbiqdxsnclcvoafqwfwcmuwitjgqghkiccwqvloqrxbfjuxwriltxhmrmfpzitkwhitwhvatmknyhzigcuxfsosxetioqfeyewoljymhdwgwvjcdhmkpdfbbztaygvbpwqxtokvidtwfdhmhpomyfhhjorsmgowikpsdgcbazapkmsjgmfyuezaamevrbsmiecoujabrbqebiydncgapuexivgvomkuiiuuhhbszsflntwruqblrnrgwrnvcwixtxycifdebgnbbucqpqldkberbovemywoaxqicizkcjbmbxikxeizmzdvjdnhqrgkkqzmspdeuoqrxswqrajxfglmqkdnlescbjzurknjklikxxqqaqdekxkzkscoipolxmcszbebqpsizhwsxklzulmjotkrqfaeivhsedfynxtbzdrviwdgicusqucczgufqnaslpwzjhgtphnovlrgz",
        },
        "output": 831
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
