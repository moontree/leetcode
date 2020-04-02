"""
Given a C++ program, remove comments from it.
The program source is an array where source[i] is the i-th line of the source code.
This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment,
which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment,
which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored.
(Here, occurrences happen in reading order: line by line from left to right.)
To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others:
if the string // occurs in a block comment, it is ignored.
Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments,
you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.
For example, source = "string s = "/* Not a comment. */";" will not be a test case.
(Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed,
so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments.
Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Example 1:
Input:
source = [
"/*Test program */",
"int main()",
"{ ",
"  // variable declaration ",
"int a, b, c;",
"/* This is a test",
"   multiline  ",
"   comment for ",
"   testing */",
"a = b + c;",
"}"
]

The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

Explanation:
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.

Example 2:
Input:
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation:
The original source string is "a/*comment\nline\nmore_comment*/b",
where we have bolded the newline characters.
After deletion, the implicit newline characters are deleted, leaving the string "ab",
which when delimited by newline characters becomes ["ab"].
Note:

The length of source is in the range [1, 100].
The length of source[i] is in the range [0, 80].
Every open block comment is eventually closed.
There are no single-quote, double-quote, or control characters in the source code.
"""


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        print(source)
        res = []
        comment_flag = None
        tmp = ''
        for s in source:
            i = 0
            while i < len(s):
                c = s[i]
                cc = s[i: i + 2]
                if comment_flag:
                    if comment_flag == '//':
                        res.append(tmp)
                        tmp = ''
                        comment_flag = None
                        break
                    else:
                        if cc == '*/':
                            i += 2
                            comment_flag = None
                        else:
                            i += 1
                else:
                    if cc == '//':
                        comment_flag = cc
                        i += 2
                    elif cc == '/*':
                        comment_flag = '/*'
                        i += 2
                    else:
                        tmp += c
                        i += 1
            if comment_flag:
                pass
            else:
                res.append(tmp)
                tmp = ''
        res = [i for i in res if i]
        print(res)
        return res




examples = [
    {
        "input": {
            "source": ["a/*comment", "line", "more_comment*/b"]
        },
        "output": ["ab"]
    },{
        "input": {
            "source": ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

        },
        "output": ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        print func(**example['input']) == example['output']