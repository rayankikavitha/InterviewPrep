"""

https://leetcode.com/problems/the-skyline-problem/description/
https://www.geeksforgeeks.org/divide-and-conquer-set-7-the-skyline-problem/
https://briangordon.github.io/2014/08/the-skyline-problem.html
input = [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] - [x,y,h]
output = [ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ] [x,y]

Exact explanation for the below code : https://leetcode.com/problems/the-skyline-problem/discuss/61194

1) sort the critical points(starting points of rectangle)
2) scan them from left to right
3) when we encounter the left edge, we add the rectangle to the heap with its height as the key.
4) when we encounter the right edge of a rectangle, we remove that rectangle from the heap.
5) Any time we encounter a critical point, after updating the heap, we set the height of that critical point to the value peeked from the top of the heap
 after updating the heap we set the height of that critical point to the value peeked from the top of the heap.

Tushar Roy skyline problem: https://www.youtube.com/watch?v=GSBLe8cKu0s&t=237s

Below solution:
It sweeps from left to right. But it doesn't only keep heights of alive buildings in the priority queue and it doesn't remove them as soon as their building is left behind.
Instead,( height, right) pairs are kept in the priority queue, and they stay in their as long as there is a larger height, not until building left behind.
In each loop, we first check what has the smaller x-coordinate, adding the next building from the input or removing the next building from the queue.
In case of a tie, adding buildings wins. We then either add all input buildings starting at that x-coordinate or we remove all queued buildings ending at that x-coordinate or earlier.
(Remember we keep buildings in the queue as long as they are under the roof of a larger actually alive building) And then, if the current maximum height in the queue differs
from the last in the skyline, we add it to the skyline.



"""


class BuildingPoint(object):
    def __init__(self, point, is_start, height):
        self.point = point
        self.is_start = is_start
        self.height = height


def basic_getskyline(buildings):
    """
    :param lrh: list of x1,x2,h
    :return: critical starting points of a skyline
    """
    skyline = []
    i,n = 0,len(buildings)
    liveheap=[]
    building_points=[]
    # build (x1,h,start), (x2,h,end) for each given (x1,x2,h) tuple Start = 1 and end = 0
    for building in buildings:
        building_points.append(BuildingPoint(building[0], True, building[2]))
        building_points.append(BuildingPoint(building[1], False, building[2]))

    building_points = sorted(building_points)

    queue = {}
    queue[0] = 1
    prev_max_height = 0
    result = []
    for building_point in building_points:
        if building_point.is_start:
            if building_point.height in queue:
                queue[building_point.height] = queue[building_point.height] + 1
            else:
                queue[building_point.height] = 1
        else:
            if queue[building_point.height] == 1:
                del queue[building_point.height]
            else:
                queue[building_point.height] = queue[building_point.height] - 1

        current_max_height = max(queue.keys())

        if prev_max_height != current_max_height:
            result.append([building_point.point, current_max_height])
            prev_max_height = current_max_height
    return result


from heapq import *

def getSkyline(LRH):
    skyline = []
    i, n = 0, len(LRH)
    liveHR = []
    while i < n or liveHR:
        if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
            x = LRH[i][0]
            while i < n and LRH[i][0] == x:
                heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                i += 1

        else:
            x = -liveHR[0][1]
            while liveHR and -liveHR[0][1] <= x:
                heappop(liveHR)

        print liveHR
        height = len(liveHR) and -liveHR[0][0]
        print height

        if not skyline or height != skyline[-1][1]:
            skyline += [x, height],
        print skyline
    return skyline

#print getSkyline([ [2, 9, 10], [3, 7, 15], [5 ,12 ,12], [15 ,20, 10], [19, 24, 8] ] )
print basic_getskyline( [[2, 9, 10], [3, 7, 15], [5 ,12 ,12], [15 ,20, 10], [19, 24, 8] ])

# test edge cases, where two buildings of different height start or end  at the same x - coordinate
print basic_getskyline( [[2, 7, 10], [2, 9, 15]]) # beginning positions are same with different heights
print basic_getskyline( [[2, 9, 15], [5, 9, 10]]) # ending positions are same with different heights
print basic_getskyline( [[2, 9, 15], [9, 12, 10]]) # building 1 is ending which is the starting point for building 2

