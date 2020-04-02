"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

"""


res = []


def restore_ip_addresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    restore_ip(s, [])


def is_valid(s):
    if len(s) > 1 and s[0] == '0':
        return False
    else:
        if 0 <= int(s) < 256:
            return True
    return False


def restore_ip(s, previous):
    if len(s) > 3 * (4 - len(previous)):
        return
    if len(previous) == 4:
        if len(s) == 0:
            res.append(".".join(previous[:]))
            return
        else:
            return
    else:
        for i in range(min(3, len(s))):
            if is_valid(s[: i + 1]):
                previous.append(s[: i + 1])
                restore_ip(s[i + 1:], previous)
                previous.pop()


examples = [
    {
        "s": "25525511135"
    }, {
        "s": "1123112"
    }, {
        "s": "010010"
    }
]


for example in examples:
    res = []
    restore_ip_addresses(example["s"])
    print res
