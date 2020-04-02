"""
Given a List of words,
return the words that can be typed using letters of alphabet on
only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""


def find_words(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    records = {}
    for i, s in enumerate(rows):
        for c in s:
            records[c] = i
    res = []
    for word in words:
        l = None
        valid = True
        for c in word:
            c = c.lower()
            if l is None:
                l = records[c]
            else:
                if records[c] != l:
                    valid = False
                    break
        if valid:
            res.append(word)
    return res


examples = [
    {
        "words": ["Hello", "Alaska", "Dad", "Peace"],
        "output": ["Alaska", "Dad"]
    }
]


for example in examples:
    print find_words(example["words"])