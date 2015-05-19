# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    @staticmethod
    def merge(intervals):
        intervals.sort(key = lambda x:x.start)
        length=len(intervals)
        res=[]
        for i in range(length):
            if res==[]:
                res.append(intervals[i])
            else:
                size=len(res)
                if res[size-1].start<=intervals[i].start<=res[size-1].end:
                    res[size-1].end=max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res

if __name__ == '__main__':
    intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
    result = Solution.merge(intervals)