"""
Given words first and second,
consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.

For each such occurrence,
add "third" to the answer,
and return the answer.



Example 1:

Input:
    text = "alice is a good girl she is a good student", first = "a", second = "good"
Output:
    ["girl","student"]

Example 2:

Input:
    text = "we will we will rock you", first = "we", second = "will"
Output:
    ["we","rock"]


Note:

    1 <= text.length <= 1000
    text consists of space separated words, where each word consists of lowercase English letters.
    1 <= first.length, second.length <= 10
    first and second consist of lowercase English letters.
"""


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        res = []
        words = text.split()
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
        return res


examples = [
    {
        "input": {
            "text": "alice is a good girl she is a good student",
            "first": "a",
            "second": "good"
        },
        "output": ["girl", "student"]
    }, {
        "input": {
            "text": "we will we will rock you",
            "first": "we",
            "second": "will"
        },
        "output": ["we", "rock"]
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
