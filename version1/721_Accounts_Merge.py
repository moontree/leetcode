"""
Given a list accounts,
each element accounts[i] is a list of strings,
where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some email that is common to both accounts.
Note that even if two accounts have the same name,
they may belong to different people as people could have the same name.
A person can have any number of accounts initially,
but all of their accounts definitely have the same name.

After merging the accounts,
return the accounts in the following format:
the first element of each account is the name,
and the rest of the elements are emails in sorted order.

The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]
Output: [
["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
["John", "johnnybravo@mail.com"],
["Mary", "mary@mail.com"]
]

Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer
[['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        c = len(accounts)
        names = []
        mails = {}
        parents = [i for i in range(c)]
        for i, account in enumerate(accounts):
            names.append(account[0])
            min_val = i
            for mail in account[1:]:
                p = mails.get(mail, i)
                while parents[p] < p:
                    p = parents[p]
                min_val = min(p, min_val)
            for mail in account[1:]:
                p = mails.get(mail, i)
                while parents[p] < p:
                    p = parents[p]
                mails[mail] = min_val
                parents[p] = min_val
            # print(i, account[1:], mails, parents)
        # print '-------------'
        # print(mails)
        # print(parents)
        cache = {}
        for mail in mails:
            p = mails[mail]
            while p > parents[p]:
                p = parents[p]
            if p in cache:
                cache[p].append(mail)
            else:
                cache[p] = [mail]
        ans = []
        for k in cache:
            mailss = cache[k]
            mailss.sort()
            ans.append([names[k]] +  [m for m in mailss])
        # print(ans)
        return ans


examples = [
    {
        "input": {
            "accounts": [
                ["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]
            ]
        },
        "output": [
            ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
            ["John", "johnnybravo@mail.com"],
            ["Mary", "mary@mail.com"]
        ]
    },{
        "input": {
            "accounts": [
                ["David", "David0@m.co", "David1@m.co"],
                ["David", "David3@m.co", "David4@m.co"],
                ["David", "David4@m.co", "David5@m.co"],
                ["David", "David2@m.co", "David3@m.co"],
                ["David", "David1@m.co", "David2@m.co"]
            ]
        },
        "output": [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
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