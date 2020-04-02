"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character,
then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1.
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, (H2O2) and (H2O2)3 are formulas.

Given a formula,
output the count of all elements as a string in the following form: the first name (in sorted order),
followed by its count (if that count is more than 1),
followed by the second name (in sorted order),
followed by its count (if that count is more than 1), and so on.

Example 1:
Input:
    formula = "H2O"
Output:
    "H2O"
Explanation:
    The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input:
    formula = "Mg(OH)2"
Output:
    "H2MgO2"
Explanation:
    The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input:
    formula = "K4(ON(SO3)2)2"
Output:
    "K4N2O14S4"
Explanation:
    The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Note:

All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.

"""


examples = [
    {
        "input": {
            "formula": "H2O"
        },
        "output": "H2O"
    }, {
        "input": {
            "formula": "Mg(OH)2"
        },
        "output": "H2MgO2"
    }, {
        "input": {
            "formula": "K4(ON(SO3)2)2"
        },
        "output": "K4N2O14S4"
    }, {
        "input": {
            "formula": "H11He49NO35B7N46Li20"
        },
        "output": "B7H11He49Li20N47O35"
    },
]

import copy


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        formula += 'A'
        mid = []
        cur_count = {}
        atom = ''
        count = ''
        block_flag = False

        def handle_end(block_flag):
            if not block_flag:
                if atom:
                    nc = int(count) if count else 1
                    cur_count[atom] = cur_count.get(atom, 0) + nc
            if block_flag:
                block_count = int(count) if count else 1
                tmp = mid.pop()
                for k in cur_count:
                    cur_count[k] = cur_count[k] * block_count + tmp.get(k, 0)
                for k in tmp:
                    if k not in cur_count:
                        cur_count[k] = tmp[k]
                block_flag = False
            return block_flag

        for c in formula:
            if c.isupper():
                block_flag = handle_end(block_flag)
                atom = c
                count = ''
            elif c.islower():
                atom += c
            elif c.isdigit():
                count += c
            if c == '(':
                block_flag = handle_end(block_flag)
                mid.append(copy.copy(cur_count))
                cur_count = {}
                atom = ''
                count = ''
            elif c == ')':
                block_flag = handle_end(block_flag)
                block_flag = True
                count = ''
        tmp = [[k, cur_count[k]] for k in cur_count]
        tmp.sort()
        res = ''
        for k, v in tmp:
            if v == 1:
                res += k
            else:
                res += '%s%d' % (k, v)
        return res


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']