"""
Sometimes people repeat letters to represent extra feeling,
such as "hello" -> "heeellooo", "hi" -> "hiiii".
In these strings like "heeellooo",
we have groups of adjacent letters that are all the same:
"h", "eee", "ll", "ooo".

For some given string S,
a query word is stretchy if it can be made to be equal to S
by any number of applications of the following extension operation:
choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello",
we could do an extension on the group "o" to get "hellooo",
but we cannot get "helloo" since the group "oo" has size less than 3.
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations:
query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy.


Example:
Input:
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
Output:
    1
Explanation:
    We can extend "e" and "o" in the word "hello" to get "heeellooo".
    We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Notes:

    0 <= len(S) <= 100.
    0 <= len(words) <= 100.
    0 <= len(words[i]) <= 100.
    S and all words in words consist only of lowercase letters

"""


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def count(word):
            tags = []
            tmp, count = None, 0
            for c in word:
                if tmp is None:
                    count += 1
                    tmp = c
                elif c == tmp:
                    count += 1
                else:
                    tags.append([tmp, count])
                    tmp, count = c, 1
            tags.append([tmp, count])
            return tags

        tag_s = count(S)
        print tag_s
        res = 0
        for word in words:
            tag_w = count(word)
            valid = True
            cc = 0
            if len(tag_s) != len(tag_w):
                continue
            for ts, tw in zip(tag_s, tag_w):
                if ts[0] != tw[0]:
                    valid = False
                    break
                if ts[1] < 3 and (tw[1] != ts[1]):
                    valid = False
                    break
                if ts[1] > 2 and tw[1] <= ts[1]:
                    cc += 1
            if valid and cc:
                res += 1
        return res


examples = [
    {
        "input": {
            "S": "heeellooo",
            "words": ["hello", "hi", "helo"],
        },
        "output": 1
    }, {
        "input": {
            "S": "heeelllooo",
            "words": ["hello", "hi", "helo"],
        },
        "output": 2
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']