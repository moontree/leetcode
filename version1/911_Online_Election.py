"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function:
TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.
In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input:
["TopVotedCandidate","q","q","q","q","q","q"],
[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].

"""
import bisect


class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.persons = persons
        self.leadings = []
        cache = {}
        count = 0
        prev = None
        for v in self.persons:
            cache[v] = cache.get(v, 0) + 1
            if cache[v] >= count:
                prev = v
                self.leadings.append(prev)
                count = cache[v]
            else:
                self.leadings.append(prev)

        print(times)
        print(persons)

        print(self.leadings)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = bisect.bisect_right(self.times,t)
        # print(t, idx)
        return self.leadings[idx - 1]


examples = [
    {
        "input": {
            "persons": [0, 1, 1, 0, 0, 1, 0],
            "times": [0, 5, 10, 15, 20, 25, 30],
            "querys": [3, 12, 25, 15, 24, 8]
        },
        "output": [0, 1, 1, 0, 0, 1]
    }, {
        "input": {
            "persons": [0, 0, 0, 0, 1],
            "times": [0, 6, 39, 52, 75],
            "querys": [45, 49, 59, 68, 42, 37, 99, 26, 78, 43]
        },
        "output": [0,0,0,0,0,0,0,0,0,0]
    }
]


import time
if __name__ == '__main__':
    for example in examples:
        print '----------'
        obj = TopVotedCandidate(example["input"]["persons"], example["input"]["times"])
        for query, res in zip(example["input"]["querys"], example["output"]):
            print obj.q(query), obj.q(query) == res

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)