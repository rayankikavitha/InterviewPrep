"""
Popular Facebook problem
Input may or may not be sorted or have duplicates
Represent input stream as an array. Don't rely on size


"""
import heapq


def topK(iStream, iK):
    h = [iStream[0]]
    res = []
    for each in iStream[1:]:
        # heap root is at 0
        # insert only if the incoming value is greater or length of the heap is less than iK
        if each > h[0] or len(h) < iK:
            heapq.heappush(h, each)
        if len(h) > iK:
            heapq.heappop(h)
    while iK > 0:
        res.append(heapq.heappop(h))
        iK -= 1
    return res[::-1]
