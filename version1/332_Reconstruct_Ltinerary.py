"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to],
reconstruct the itinerary in order.
All of the tickets belong to a man who departs from JFK.
 Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.
 For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
import collections


def find_itinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []

    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)

    visit('JFK')
    return route[::-1]


def dfs(records, reached, count, pre, cur, res):
    if len(res):
        return
    if len(pre) == count:
        res.append(pre[:])
        return
    if records.get(cur):
        for i in xrange(len(records[cur])):
            t = records[cur][i]
            if not reached[cur][i]:
                reached[cur][i] = True
                pre.append(t)
                dfs(records, reached, count, pre, t, res)
                pre.pop()
                reached[cur][i] = False
    else:
        return


examples = [
    {
        "tickets": [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
        "res": ["JFK", "MUC", "LHR", "SFO", "SJC"]
    }, {
        "tickets": [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],
        "res": ["JFK","ATL","JFK","SFO","ATL","SFO"]
    }, {
        "tickets": [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"], ["KUL", "APP"]],
        "res": ["JFK","NRT","JFK","KUL"]
    }, {
        "tickets": [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]],
        "res": ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
    }
]


for example in examples:
    print "-----"
    print find_itinerary(example["tickets"])
