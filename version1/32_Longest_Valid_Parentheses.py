'''

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

examples = [
    {
        'input': '(()',
        'output': 2
    },{
        'input': ')()())',
        'output': 4
    },{
        'input': '()(()',
        'output': 2
    },{
        'input': '()()())()',
        'output': 6,
    },{
        'input': "(()(((()",
        'output': 2
    },{
        'input': '',
        'output': 0,
    },{
        'input': '(()()',
        'output': 4,
    },{
        'input': '(()(()))()',
        'output': 10,
    },{
        'input': '()()()()',
        'output': 8
    },{
        'input': ")(((((()())()()))()(()))(",
        'output': 22
    }
]

'''
find valid and try to connect them
'''

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    records = {}
    count = len(s)
    index = 0

    stack = []
    while index < count:
        if s[index] == '(':
            stack.append(index)
        else:
            if len(stack) > 0:
                matched_index = stack.pop()
                records[matched_index] = index - matched_index + 1
        index += 1

    for k in records:
        index = k
        while records[index] > 0 and index < count:
            next_index = index + records[index]
            continue_length = records.get(next_index, 0)
            if continue_length > 0:
                records[k] += continue_length
                records[next_index] = 0
            else:
                break
    length = [records[k] for k in records]
    if len(length) == 0:
        return 0
    return max(length)

'''
take use of break indexs
'''

def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    count = len(s)
    longest = 0
    stack = []
    for i in range(0, count):
        if s[i] == '(':
            stack.append(i)
        else:
            last_start = -1
            if len(stack):
                if s[stack[-1]] == '(':
                    stack.pop()
                    if len(stack):
                        last_start = stack[-1]
                    longest = max(i - last_start, longest)
                else:
                    stack.append(i)
            else:
                stack.append(i)

    return longest

for example in examples:
    print '------ testing example ------', example['input']
    res = longestValidParentheses(example['input'])
    print res == example['output'], 'output is ', res, ',expect is ', example['output']