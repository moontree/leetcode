"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""
import re


def decode_string(s):
    """
    :type s: str
    :rtype: str
    """
    return decode_helper(list(s)[::-1])
    stack = [""]
    times = []
    ss = ""
    is_num = True
    for c in s:
        if c == "[":
            stack.append("")
            times.append(int(ss))
            ss = ""
        elif c == "]":
            stack[-1] += ss
            ts = stack.pop()
            stack[-1] += times.pop() * ts
            ss = ""
        elif c.isdigit():
            if is_num:
                ss += c
            else:
                stack[-1] += ss
                ss = c
                is_num = True
        else:
            is_num = False
            ss += c
    stack[-1] += ss
    # print stack
    return stack[-1]


def decode_string_re(s):
    while '[' in s:
        # print re.match(r'(\d+)\[([a-z]*)\]', s)
        s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    return s


def decode_helper(s):
    res = ""
    while s:
        num = ""
        while s and s[-1].isdigit():
            num += s.pop()
        if num:
            s.pop()
            res += int(num) * decode_helper(s)
        else:
            c = s.pop()
            if c == "]":
                break
            elif c == "[":
                pass
            else:
                res += c
    return res


examples = [
    {
        "s": "3[a]2[bc]"
    }, {
        "s": "3[a2[c]]"
    }, {
        "s": "2[abc]3[cd]ef"
    }, {
        "s": "100[a]"
    },
]


for example in examples:
    print "----"
    print decode_string(example["s"])