"""
Given a string of numbers and operators,
return all possible results from computing all the different possible ways to group numbers and operators.
The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""


def diff_ways_to_compute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    res = []
    for i, c in enumerate(input):
        if c in "+-*":
            left = input[: i]
            right = input[i + 1:]
            for a in diff_ways_to_compute(left):
                for b in diff_ways_to_compute(right):
                    if c == "+":
                        res.append(a + b)
                    elif c == "-":
                        res.append(a - b)
                    else:
                        res.append(a * b)
    return res or [int(input)]


examples = [
    {
        "input": "2-1-1",
        "res": [0, 2]
    }, {
        "input": "2*3-4*5",
        "res": [-34, -14, -10, -10, 10]
    },
]


for example in examples:
    print diff_ways_to_compute(example["input"])
