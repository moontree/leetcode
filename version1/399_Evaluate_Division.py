"""
Equations are given in the format A / B = k,
 where A and B are variables represented as strings,
 and k is a real number (floating point number).
 Given some queries, return the answers.
 If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is:
vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries ,
where equations.size() == values.size(), and the values are positive.
 This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
"""


def calc_equation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    vals = {}
    relations = {}
    for i in xrange(len(equations)):
        dividend, divisor = equations[i]
        val = values[i]
        relations[dividend] = relations.get(dividend, []) + [[divisor, val]]
        relations[divisor] = relations.get(divisor, []) + [[dividend, 1.0 / val]]
    tmp = relations.keys()
    stack = [tmp[0]]
    group = 0
    while stack or relations:
        if not stack:
            stack = [relations.keys()[0]]
            group += 1
        cur = stack.pop(0)
        if vals.get(cur) is None:
            vals[cur] = [1.0, group]
        val = vals[cur][0]
        if relations.get(cur) is None:
            continue
        for ss, ratio in relations[cur]:
            vals[ss] = [val / ratio, group]
            stack.append(ss)
        del relations[cur]
    # print vals
    res = []
    for dividend, divisor in queries:
        if vals.get(dividend) is None or vals.get(divisor) is None:
            res.append(-1.0)
        else:
            if vals[dividend][1] == vals[divisor][1]:
                res.append(vals[dividend][0] / vals[divisor][0])
            else:
                res.append(-1.0)
    return res


examples = [
    {
        "input": {
            "equations": [["a", "b"], ["b", "c"]],
            "values": [2.0, 3.0],
            "queries": [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        },
        "output": [6.0, 0.5, -1.0, 1.0, -1.0]
    }, {
        "input": {
            "equations": [["a", "b"], ["e", "f"], ["b", "e"]],
            "values": [3.4, 1.4, 2.3],
            "queries": [["b", "a"], ["a", "f"], ["f", "f"], ["e", "e"], ["c", "c"], ["a", "c"], ["f", "e"]]
        },
        "output": [0.29411764705882354, 10.947999999999999, 1.0, 1.0, -1.0, -1.0, 0.7142857142857143]
    }, {
        "input": {
            "equations": [["a", "b"], ["b", "c"], ["bc", "cd"]],
            "values": [1.5, 2.5, 5.0],
            "queries": [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        },
        "output": [3.75, 0.4, 5.0, 0.2]
    }, {
        "input": {
            "equations": [["a", "b"], ["c", "d"]],
            "values": [1.0, 1.0],
            "queries": [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]
        },
        "output": [-1.0, -1.0, 1.0, 1.0]
    }
]


for example in examples:
    print "----"
    print calc_equation(**example["input"])
