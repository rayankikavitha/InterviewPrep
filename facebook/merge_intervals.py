# Definition for an interval.
"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].





class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e
"""



def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    result=[]
    for each in sorted(intervals, key = lambda x:x[0]):
        # compare the incoming interval with the last processed interval.
        # current interval begin is less than result end.
        print each
        print result
        if result and each[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], each[1])
            print result
        else:
            result.append(each)
    return result

input1 = [[1,3],[2,6],[8,10],[15,18]]
input2 = [[1,3],[2,6],[5,10],[15,18]]


print merge(input1)
print merge(input2)
