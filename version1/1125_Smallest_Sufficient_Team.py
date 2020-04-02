"""
In a project, you have a list of required skills req_skills, and a list of people.
The i-th person people[i] contains a list of skills that person has.

Consider a sufficient team:
a set of people such that for every required skill in req_skills,
there is at least one person in the team who has that skill.
We can represent these teams by the index of each person:
for example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person.

You may return the answer in any order.  It is guaranteed an answer exists.



Example 1:

Input:
    req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output:
    [0,2]

Example 2:

Input:
    req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
    people = [["algorithms","math","java"],["algorithms","math","reactjs"],
    ["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

Output: [1,2]

Constraints:

    1 <= req_skills.length <= 16
    1 <= people.length <= 60
    1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
    Elements of req_skills and people[i] are (respectively) distinct.
    req_skills[i][j], people[i][j][k] are lowercase English letters.
    Every skill in people[i] is a skill in req_skills.
    It is guaranteed a sufficient team exists.
"""


class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        cache = {}
        for i, v in enumerate(req_skills):
            cache[v] = 1 << i
        n = len(req_skills)
        dp = [list(range(len(people))) for _ in range(1 << n)]
        dp[0] = []
        for i, p in enumerate(people):
            skills = 0
            for skill in p:
                skills |= cache.get(skill, 0)
            for k, v in enumerate(dp):
                new_skills = k | skills
                if new_skills != k and len(v) < len(dp[new_skills]) - 1:
                    dp[new_skills] = v + [i]
        return dp[-1]


examples = [
    {
        "input": {
            "req_skills": ["java", "nodejs", "reactjs"],
            "people": [["java"], ["nodejs"], ["nodejs", "reactjs"]]
        },
        "output": [0, 2]
    }, {
        "input": {
            "req_skills": ["algorithms", "math", "java", "reactjs", "csharp", "aws"],
            "people": [
                ["algorithms", "math", "java"],
                ["algorithms", "math", "reactjs"],
                ["java", "csharp", "aws"],
                ["reactjs", "csharp"],
                ["csharp", "math"],
                ["aws", "java"]
            ]
        },
        "output": [1, 2]
    }, {
        "input": {
            "req_skills": ["uhppib", "mgdipkgt", "vaostwmycy", "bjwxnfbbubpnd"],
            "people": [
                ["vaostwmycy"],
                ["mgdipkgt"],
                ["bjwxnfbbubpnd"],
                [],
                ["uhppib"]
            ]
        },
        "output": [0, 1, 2, 4]
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start
