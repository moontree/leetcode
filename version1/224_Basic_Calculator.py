"""
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

"""


def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    res, num, sign, stack = 0, 0, 1, [1]
    for c in s + "+":
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "+" or c == "-":
            res += num * sign * stack[-1]
            sign = 1 if c == "+" else -1
            num = 0
        elif c == "(":
            stack.append(sign * stack[-1])
            sign = 1
        elif c == ")":
            res += num * sign * stack[-1]
            num = 0
            stack.pop()
        else:
            pass
    return res


def calculate_2(s):
    nums = []
    ops = []
    num = ""
    priors = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "(": 3,
        ")": 3
    }
    for p in s:
        if "0" <= p <= "9":
            num += p
        else:
            if len(num):
                nums.append(int(num))
            num = ""
            if p == " ":
                continue
            elif p == "+" or p == "-":
                if len(ops) and ops[-1] != "(" and priors[p] < priors[ops[-1]]:
                    nums.append(ops.pop())
                ops.append(p)
            elif p == "(":
                ops.append(p)
                pass
            elif p == ")":
                while len(ops) and ops[-1] != "(":
                    nums.append(ops.pop())
                ops.pop()
                pass
            else:
                pass
    if len(num):
        nums.append(int(num))
    while len(ops):
        nums.append(ops.pop())
    stack = []
    for p in nums:
        if p == "+":
            right = stack.pop()
            left = stack.pop()
            stack.append(left + right)
        elif p == "-":
            right = stack.pop()
            left = stack.pop()
            stack.append(left - right)
        else:
            stack.append(p)
    return stack[0]


examples = [
    {
        "s": "1 + 1",
        "res": 2
    }, {
        "s": " 2-(1 + 2) ",
        "res": 3
    }
]


for example in examples:
    print calculate(example["s"])
