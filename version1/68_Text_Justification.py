"""
Given an array of words and a length L,
format the text such that each line has exactly L characters
and is fully (left and right) justified.

You should pack your words in a greedy approach;
that is, pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


def full_justify(words, max_width):
    """
    :type words: List[str]
    :type max_width: int
    :rtype: List[str]
    """
    res, row, words_length = [], [], 0
    for w in words:
        if words_length + len(row) + len(w) > max_width:
            for i in range(max_width - words_length):
                row[i % (len(row) - 1 or 1)] += ' '
            res.append(''.join(row))
            row, words_length = [], 0
        row.append(w)
        words_length += len(w)
    row_str = " ".join(row)
    row_str += "".join([" "] * (max_width - len(row_str)))
    res.append(row_str)
    return res


examples = [
    {
        "words": ["This", "is", "an", "example", "of", "text", "justification."],
        "L": 16
    }, {
        "words": ["This", "is", "an", "example", "of", "text", "justification."],
        "L": 15
    }, {
        "words": ["a", "b", "c", "d", "e"],
        "L": 2
    }, {
        "words": ["What", "must", "be", "shall", "be."],
        "L": 12
    }, {
        "words": ["Don't", "go", "around", "saying", "the", "world", "owes", "you", "a", "living;",
                  "the", "world", "owes", "you", "nothing;", "it", "was", "here", "first."],
        "L": 30
    }
]


for example in examples:
    print full_justify(example["words"], example["L"])
