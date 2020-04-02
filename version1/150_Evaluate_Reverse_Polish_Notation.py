"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

"""


def eval_RPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    operations = {
        "*": lambda x, y: x * y,
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "/": lambda x, y: float(x) / y
    }

    stack = []
    for token in tokens:
        if token not in operations:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            result = operations[token](left, right)
            stack.append(int(result))
    return stack.pop()


examples = [
    {
        "tokens": ["2", "1", "+", "3", "*"],
        "res": 9
    }, {
        "tokens": ["4", "13", "5", "/", "+"],
        "res": 6
    }, {
        "tokens": ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        "res": 22
    }, {
        "tokens": ["10"],
        "res": 10
    }
]


for example in examples:
    print eval_RPN(example["tokens"])
