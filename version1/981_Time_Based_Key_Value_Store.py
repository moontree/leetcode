"""
Create a timebased key-value store class TimeMap, that supports two operations.

1. set(string key, string value, int timestamp)

Stores the key and value, along with the given timestamp.

2. get(string key, int timestamp)

Returns a value such that set(key, value, timestamp_prev) was called previously, with timestamp_prev <= timestamp.

If there are multiple such values, it returns the one with the largest timestamp_prev.
If there are no values, it returns the empty string ("").


Example 1:

Input:
    inputs = ["TimeMap","set","get","get","set","get","get"],
    inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
Output:
    [null,null,"bar","bar",null,"bar2","bar2"]
Explanation:
    TimeMap kv;
    kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
    kv.get("foo", 1);  // output "bar"
    kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2,
    then the only value is at timestamp 1 ie "bar"
    kv.set("foo", "bar2", 4);
    kv.get("foo", 4); // output "bar2"
    kv.get("foo", 5); //output "bar2"

Example 2:

Input:
    inputs = ["TimeMap","set","set","get","get","get","get","get"],
    inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Output:
    [null,null,null,"","high","high","low","low"]


Note:
    All key/value strings are lowercase.
    All key/value strings have length in the range [1, 100]
    The timestamps for all TimeMap.set operations are strictly increasing.
    1 <= timestamp <= 10^7
    TimeMap.set and TimeMap.get functions will be called a total of 120000 times (combined) per test case.
"""
import bisect


class TimeMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = {}
        self.timestamps = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.vals:
            self.vals[key] = [value]
            self.timestamps[key] = [timestamp]
        else:
            self.vals[key].append(value)
            self.timestamps[key].append(timestamp)
        print self.vals

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.vals:
            return ""
        idx = bisect.bisect(self.timestamps[key], timestamp)
        if idx == 0:
            return ""
        else:
            return self.vals[key][idx - 1]


if __name__ == '__main__':
    kv = TimeMap()
    print kv.set("ctondw", "ztpearaw", 1) # store the key "foo" and value "bar" along with timestamp = 1
    print kv.set("vrobykydll", "hwliiq", 2) # store the key "foo" and value "bar" along with timestamp = 1
    print kv.set("gszaw", "ztpearaw", 3) # store the key "foo" and value "bar" along with timestamp = 1
    print kv.set("ctondw", "gszaw", 4) # store the key "foo" and value "bar" along with timestamp = 1
    print kv.get("gszaw", 5) # output "bar"
    print kv.get("ctondw", 6) # output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
    print kv.get("ctondw", 7) # output "bar2"
    print kv.get("gszaw", 8) #/output "bar2"