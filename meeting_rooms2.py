"""
given a list of start, end times, find no.of meeting rooms needed

given =[[0,30],[5,10],[15,20]]
output = 2 meeting rooms
"""
# very intuitive
# maintain heap and insert interval end times.
# keep track of max-size of heap which is equal to meeting room count  
import heapq
def count_meeting_rooms(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    h=[nums[1][1]]
    maxrooms = 1
    for num in nums[1:]:
        if num[1] < h[0]:
            heapq.heappush(h,num[1])
            maxrooms = max(maxrooms, len(h))
            print maxrooms, h
        else:
            heapq.heappop(h)
            heapq.heappush(h,num[1])
    return maxrooms

print count_meeting_rooms([[1,4],[5,7],[6,8],[9,12],[10,11],[11,12]])




# below approach is not easy to understand

# Very similar with what we do in real life. Whenever you want to start a meeting,
# you go and check if any empty room available (available > 0) and
# if so take one of them ( available -=1 ). Otherwise,
# you need to find a new room someplace else ( numRooms += 1 ).
# After you finish the meeting, the room becomes available again ( available += 1 ).

def minMeetingRooms(self, intervals):
    starts = []
    ends = []
    for i in intervals:
        starts.append(i.start)
        ends.append(i.end)

    starts.sort()
    ends.sort()
    s = e = 0
    numRooms = available = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            if available == 0:
                numRooms += 1
            else:
                available -= 1

            s += 1
        else:
            available += 1
            e += 1

    return numRooms