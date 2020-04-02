"""
Given a string array words,
 find the maximum value of length(word[i]) * length(word[j])
  where the two words do not share common letters.
   You may assume that each word will contain only lower case letters.
    If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

"""


def max_product(words):
    """
    :type words: List[str]
    :rtype: int
    """
    nums = []
    for word in words:
        val = 0
        for c in word:
            val |= 1 << (ord(c) - 97)
        nums.append(val)
    res = 0
    print nums
    m = len(words)
    for i in xrange(m):
        for j in xrange(i + 1, m):
            if nums[i] & nums[j] == 0:
                product = len(words[i]) * len(words[j])
                if product > res:
                    res = product
    return res


examples = [
    {
        "words": ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
        "res": 16,
    }, {
        "words": ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
        "res": 4,
    }, {
        "words": ["a", "aa", "aaa", "aaaa"],
        "res": 0,
    }
]


for example in examples:
    print max_product(example["words"])
