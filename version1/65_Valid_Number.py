"""
Validate if a given string is numeric.
"""


def is_number(s):
    """
    :type s: str
    :rtype: bool
    """
    valid_chars = {
        "0": 1,
        "1": 1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1,
        "7": 1,
        "8": 1,
        "9": 1,
        "+": 1,
        "-": 1,
        ".": 1,
        " ": 1,
        "e": 1
    }

    # remove " "
    tail = len(s) - 1
    while tail > -1 and s[tail] == " ":
        tail -= 1
    s = s[:tail + 1]
    index = 0
    while index < len(s):
        if valid_chars.get(s[index]) is None:
            return False
        else:
            if s[index] == "e":
                return False
            if s[index] == " ":
                index += 1
            else:
                break
    # print " after remove blanks", s[index:]
    # remove sign
    if index > len(s) - 1:
        return False
    if s[index] == "+" or s[index] == "-":
        index += 1
    if index > len(s) - 1:
        return False
    # find . and e
    point_num = 0
    point_index = len(s)
    e_num = 0
    e_index = len(s)
    for i in range(index, len(s)):
        if s[i] == ".":
            point_num += 1
            point_index = i
            if point_num > 1:
                return False
        if s[i] == "e":
            e_num += 1
            e_index = i
            if e_num > 1:
                return False
    if len(s) > point_index > e_index:
        return False
    if point_num:
        float_valid = is_float(s[index: point_index], s[point_index + 1: e_index])
        if e_num:
            # print " ------ find e ------", s[e_index:]
            e_valid = is_e_number(s[e_index:])
            return float_valid and e_valid
        return float_valid
    else:
        # print " ---- int base ----", s[index: e_index]
        base_valid = is_total_number(s[index: e_index])
        if e_num > 0:
            # print " ------ find e ------", s[e_index:]
            return is_e_number(s[e_index:]) and base_valid
        else:
            return base_valid


def is_float(sl, sr):
    if len(sl) == 0 and len(sr) == 0:
        return False
    if len(sl) == 0:
        return is_total_number(sr)
    if len(sr) == 0:
        return is_total_number(sl)
    return is_total_number(sl) and is_total_number(sr)


def is_e_number(s):
    if len(s):
        if s[0] == "e":
            if len(s) < 2:
                return False
            if s[1] == '+' or s[1] == "-":
                return is_total_number(s[2:])
            else:
                return is_total_number(s[1:])
        else:
            return is_total_number(s)


def is_total_number(s):
    numbers = {"0": 1, "1": 1, "2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 1, "8": 1, "9": 1}
    if len(s) == 0:
        return False
    for c in s:
        if numbers.get(c) is None:
            return False
    return True


examples = [
    {
        "s": "0000",
        "res": True
    }, {
        "s": "00 00",
        "res": False
    }, {
        "s": "e",
        "res": False
    }, {
        "s": "e-10",
        "res": False
    }, {
        "s": "1e-10",
        "res": True
    }, {
        "s": "+-123",
        "res": False
    }, {
        "s": "+31",
        "res": True
    }, {
        "s": ".",
        "res": False
    }, {
        "s": "0.",
        "res": True
    }, {
        "s": ".0",
        "res": True
    }, {
        "s": "-0.1e-1",
        "res": True
    }, {
        "s": "-0.1e",
        "res": False
    }, {
        "s": "-0.1e0",
        "res": True
    }, {
        "s": "a-0.1e0",
        "res": False
    }, {
        "s": ".1e0",
        "res": True
    }, {
        "s": "    ",
        "res": False
    }, {
        "s": "    +",
        "res": False
    }, {
        "s": "    e",
        "res": False
    }, {
        "s": "  1  ",
        "res": True
    }, {
        "s": "4.m",
        "res": False
    }, {
        "s": "3e88+9",
        "res": False
    }
]


"""
using DFA
"""


def is_number_using_dfa(s):
    # type: (str) -> bool
    # define a DFA
    state = [{},
             {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
             {'digit': 3, '.': 4},
             {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
             {'digit': 5},
             {'digit': 5, 'e': 6, 'blank': 9},
             {'sign': 7, 'digit': 8},
             {'digit': 8},
             {'digit': 8, 'blank': 9},
             {'blank': 9}]
    current_state = 1
    for c in s:
        if '9' >= c >= '0':
            c = 'digit'
        if c == ' ':
            c = 'blank'
        if c in ['+', '-']:
            c = 'sign'
        if c not in state[current_state].keys():
            return False
        current_state = state[current_state][c]
    if current_state not in [3, 5, 8, 9]:
        return False
    return True


import PIL.Image as im
for example in examples:
    res = is_number_using_dfa(example["s"])
    print example["s"], res, "expected is", example["res"]
image = im.open("valid_number_dfg.png")
image.show()
