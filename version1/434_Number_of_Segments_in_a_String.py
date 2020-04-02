"""
Count the number of segments in a string,
 where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5

"""


def count_segments(s):
    """
    :type s: str
    :rtype: int
    """
    count = 0
    l, cur, n = 0, 0, len(s)
    for i, c in enumerate(s):
        if c == " ":
            if l < i:
                count += 1
            l = i + 1
    if l < n:
        count += 1
    return count


print count_segments("Hello, my name is John")
print count_segments("Hello, my name is John  ")
print count_segments("Hello,")
print count_segments("  Hello  hn")
