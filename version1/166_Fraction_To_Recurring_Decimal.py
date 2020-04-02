"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
"""


def fraction_to_decimal(numerator, denominator):
    """
    :type numerator: int
    :type denominator: int
    :rtype: str
    """
    # simulate divide
    integer = numerator / denominator
    sign = -1 if integer < 0 else 1
    integer, numerator, denominator = abs(integer), abs(numerator), abs(denominator)
    integer = numerator / denominator
    res = "-" if sign == -1 else ""
    if numerator % denominator == 0:
        res += str(integer)
    else:
        res += str(integer) + "."
        rest = numerator % denominator
        record = {}
        fraction = ""
        repeat = ""
        while rest:
            div = (rest * 10) / denominator
            seen = record.get(rest, 0)
            if seen == 0:
                fraction += str(div)
                record[rest] = 1
            elif seen == 1:
                repeat += str(div)
                record[rest] = 2
            elif seen == 2:
                break
            rest = (rest * 10) % denominator
        if len(repeat):
            res += fraction[:-len(repeat)] + "(" + repeat + ")"
        else:
            res += fraction
    return res


examples = [
    {
        "numerator": 1,
        "denominator": 2,
        "res": '0.5',
    }, {
        "numerator": 2,
        "denominator": 1,
        "res": '2',
    }, {
        "numerator": 2,
        "denominator": 3,
        "res": '0.(6)',
    }, {
        "numerator": 11,
        "denominator": 7,
        "res": '1.(571428)',
    }, {
        "numerator": 1,
        "denominator": 6,
        "res": '0.1(6)',
    }, {
        "numerator": -3081,
        "denominator": 9900,
        "res": '0.31(12)',
    }, {
        "numerator": -1,
        "denominator": 999,
        "res": '0.31(12)',
    }
]


for example in examples:
    print "----"
    print fraction_to_decimal(example["numerator"], example["denominator"])
