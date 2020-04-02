'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

'''

examples = [
    {
        "input" : 1,
        "output" : "1"
    },{
        "input": 3,
        "output": "21"
    },{
        "input": 4,
        "output": "1211"
    },{
        "input": 5,
        "output": "111221"
    }
]

def countAndSay(n):
    if n == 1:
        return "1"
    else:
        prev_str = "1"
        for i in range(1, n):
            current_str = ""
            j = 1
            count = 1
            c = prev_str[0]
            while j < len(prev_str):
                if prev_str[j] == c:
                    count += 1
                    j += 1
                else:
                    current_str += str(count) + c
                    count = 1
                    c = prev_str[j]
                    j += 1
            current_str += str(count) + c
            prev_str = current_str
        return prev_str

for example in examples:
    print '---- test case ----', example["input"]
    print countAndSay(example["input"])