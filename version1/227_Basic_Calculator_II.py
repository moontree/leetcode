"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
"""


def calculate(s):
    res, num, stack, sign = 0, 0, [], "+"
    for c in s + "+":
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == " ":
            continue
        else:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                tmp = stack.pop()
                if tmp / num < 0 and tmp % num != 0:
                    tmp = tmp / num + 1
                else:
                    tmp = tmp / num
                stack.append(tmp)
            num = 0
            sign = c
    print stack
    return sum(stack)


examples = [
    {
        "s": "3+2*2",
        "res": 7,
    },{
        "s": "3/2",
        "res": 1,
    },{
        "s": " 3+5 / 2 ",
        "res": 5
    },{
        "s": "100000000/1/2/3/4/5/6/7/8/9/10",
        "res": 27
    },{
        "s": "14-3/2",
        "res": 13
    }
]

for example in examples:
    print calculate(example["s"])
